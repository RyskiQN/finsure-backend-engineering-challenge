from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework_json_api import views

from .forms import CreateLenderForm
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
        form = CreateLenderForm()
    return render(request, 'add_lender.html', {'form': form})


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


def edit_lender(request, pk=0):
    pass

@api_view(['GET'])
def api_root(request, format=None):
    # Create a paginator instance
    paginator = PageNumberPagination()
    # Set the page size to 5
    paginator.page_size = 5
    paginator.max_page_size = 5
    # Set the page query parameter to 'p'
    paginator.page_query_param = 'p'
    # Get the list of available endpoints
    endpoints = [
        ('posts', reverse('post-list', request=request, format=format)),
    ]
    # Paginate the endpoints list
    page = paginator.paginate_queryset(Lender.objects.all(), request)
    # Return the paginated response
    return paginator.get_paginated_response(page)

class PostList(generics.ListCreateAPIView):
    queryset = Lender.objects.all()
    serializer_class = LenderSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lender.objects.all()
    serializer_class = LenderSerializer

class PostViewSet(views.ModelViewSet):
    queryset = Lender.objects.all()
    serializer_class = LenderSerializer
