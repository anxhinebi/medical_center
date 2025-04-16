from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_home, name='blog_home'),
    path('blog/search/', views.blog_search, name='blog_search'),
    path('post/<int:pk>/', views.blog_post, name='blog_post'),
    path('discount/<int:pk>/', views.blog_discount, name='blog_discount'),
    path('job/<int:pk>/', views.blog_job, name='blog_job'),
]