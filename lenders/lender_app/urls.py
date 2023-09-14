from django.urls import path
from . import views

urlpatterns = [
    path('get_data/', views.getData),
    path('post_data/', views.postData),
    path('create', views.add_lender),
    path('list', views.list_lenders),
    path('search', views.search_lenders),
    path('', views.api_root),
    path('posting/<int:pk>', views.edit_lender, name='posting'),
    path('post_list/', views.PostList.as_view(), name='post-list'),
    path('posts/<int:pk>/', views.PostDetail.as_view(), name='post-detail'),
]