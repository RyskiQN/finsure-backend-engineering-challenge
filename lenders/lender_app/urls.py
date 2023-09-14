from django.urls import path
from . import views

urlpatterns = [
    path('get_data', views.getData, name='get'),
    path('post_data', views.postData, name='post'),
    path('create', views.create_lender, name='create'),
    path('upload_csv', views.upload_lenders, name='upload'),
    path('list', views.list_lenders, name='list'),
    path('search', views.search_lenders, name='search'),
    path('update/<int:id>', views.update_lender, name='update'),
    path('update/delete/<int:id>', views.delete_lender, name='delete'),
    path('download', views.dnload_lenders, name='download'),
]
