from django.urls import path
from . import views

urlpatterns = [
    path('get_data/', views.getData),
    path('post_data/', views.postData),
    path('create', views.add_lender, name='create'),
    path('list', views.list_lenders, name='list'),
    path('search', views.search_lenders, name='search'),
    path('update/<int:id>', views.update_lender, name='update'),
    path('update/delete/<int:id>', views.delete_lender, name='delete'),
]
