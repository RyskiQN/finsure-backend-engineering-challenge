from django.shortcuts import render, redirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework_json_api import views

from .forms import CreateLenderForm, UpdateLenderForm
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


def add_lender(request):
    if request.method == 'POST':
        form = CreateLenderForm(request.POST)
        serializer = LenderSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()

    else:
        context = {
            {'form': CreateLenderForm()}
        }
    return render(request, 'add_lender.html', context)


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

        return redirect("list")
    else:
        context = {
            'lender': Lender.objects.get(id=id)
        }
        return render(request, 'confirm.html', context)