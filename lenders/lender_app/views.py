import csv
from django.shortcuts import render, redirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib import messages
from django.utils.encoding import smart_str
from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework_json_api import views

from .forms import *
from .serializers import LenderSerializer
from .models import Lender
from .filters import *


# Create your views here.
@api_view(['GET'])
def getData(request):
    app = Lender.objects.all()
    serializer = LenderSerializer(app, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def postData(request):
    serializer = LenderSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


def create_lender(request):
    if request.method == 'POST':
        form = CreateLenderForm(request.POST)
        serializer = LenderSerializer(data=request.POST)
        if serializer.is_valid():
            try:
                serializer.save()
            except Exception as e:
                messages.error(request, f"Lender Creation Failed!\n" +
                               f"{e}")

    else:
        form = CreateLenderForm()
    return render(request, 'create_lender.html', {'form': form})


def list_lenders(request):
    lender_list = Lender.objects.all().order_by('code')
    lender_filter = ActiveLenderFilter(request.GET, queryset=lender_list)

    paginator = Paginator(lender_filter.qs, 5)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'filter': lender_filter,
        'paginator_filter': paged_listings
    }

    if request.method == 'GET':
        print('Get')
        return render(request, 'listing.html', context)


def search_lenders(request):
    lender_list = Lender.objects.all().order_by('code')
    lender_filter = SearchLenderFilter(request.GET, queryset=lender_list)

    paginator = Paginator(lender_filter.qs, 5)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'filter': lender_filter,
        'paginator_filter': paged_listings
    }

    if request.method == 'GET':
        print('Get')
        return render(request, 'listing.html', context)


def update_lender(request, id=1):
    if request.method == 'POST':
        serializer = LenderSerializer(instance=Lender.objects.get(id=id),
                                      data=request.POST)
        if serializer.is_valid():
            serializer.save()

        return redirect("list")
    else:
        context = {
            'form': UpdateLenderForm(id=id),
            'lender': Lender.objects.get(id=id)
        }
        return render(request, 'update_lender.html', context)


def delete_lender(request, id=1):
    if request.method == 'POST':
        Lender.objects.get(id=id).delete()
        messages.success(request, 'Lender deleted successfully.')
        return redirect("list")
    else:
        context = {
            'lender': Lender.objects.get(id=id)
        }
        return render(request, 'confirm.html', context)


def upload_lenders(request):
    if request.method == 'POST':
        form = UploadLendersForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['csv_file']
            # check if it is a valid csv file
            if not csv_file.name.endswith('.csv'):
                messages.error(request, 'Please upload a valid csv file.')
                return redirect('upload')
            # read and process the csv file
            data = csv_file.read().decode('utf-8')
            lines = data.split('\n')
            # loop over the lines and save them in db
            for i, line in enumerate(lines):
                # skip empty lines
                if not line:
                    continue
                try:
                    # get the fields from each line
                    fields = line.split(',')
                    # assert + data transforms ensure data at least seems correct (there is probably a safer way to do this)
                    assert len(fields) == 5
                    # create a dictionary for the lender model fields
                    lender_dict = {}
                    lender_dict['name'] = fields[0]
                    lender_dict['code'] = fields[1]
                    lender_dict['upfront_com'] = float(fields[2])
                    lender_dict['trial_com'] = float(fields[3])
                    lender_dict['active'] = bool(fields[4])
                    # create or update the lender model instance
                    lender, created = Lender.objects.update_or_create(
                        name=lender_dict['name'],
                        defaults=lender_dict
                    )
                except Exception as e:
                    if i == 0:  # ignore a failure on the first line in case they are titles
                        continue
                    else:
                        messages.error(request, f'Failed to parse line {i} of the chosen CSV file!')
                        return redirect('upload')

            messages.success(request, 'Lenders uploaded successfully.')
            return redirect('create')
    else:
        form = UploadLendersForm()
    return render(request, 'upload_lenders.html', {'form': form})


def dnload_lenders(request):
    # create a HttpResponse object with the content_type set to 'text/csv'
    response = HttpResponse(content_type='text/csv')
    # set the Content-Disposition header to 'attachment; filename="lenders.csv"'
    response['Content-Disposition'] = 'attachment; filename="lenders.csv"'
    # create a csv.writer object with the response as the file-like object
    writer = csv.writer(response)
    # write the header row with the names of the fields in your lender model
    writer.writerow([
        smart_str(u"Name"),
        smart_str(u"Code"),
        smart_str(u"Upfront Commission Rate"),
        smart_str(u"Trial Commission Rate"),
        smart_str(u"Active"),
    ])
    # query the database for all the lenders and loop over them
    lenders = Lender.objects.all()
    for lender in lenders:
        # write a row of data with the values of its fields
        writer.writerow([
            smart_str(lender.name),
            smart_str(lender.code),
            smart_str(lender.upfront_com),
            smart_str(lender.trial_com),
            smart_str(lender.active),
        ])
    # return the response object from the view
    return response