from django.contrib import admin
from django.urls import path
from . import views
app_name='HomePage'
urlpatterns = [
    path('',views.main_index,name='index'),
    path('about_us',views.about_us,name='about_us'),
    path('listing',views.listing,name='listing'),
    path('contact',views.contact,name='contact'),
    path('blog',views.blog,name='blog'),
    path('single_listing',views.single_listing,name='single_listing'),
    path('single_blog',views.single_blog,name='single_blog'),
]
