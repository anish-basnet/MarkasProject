from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings;
from django.conf.urls.static import static;




app_name='HomePage'
urlpatterns = [
    path('',views.main_index,name='index'),
    path('about_us',views.about_us,name='about_us'),
    path('listing',views.listing,name='listing'),
    path('contact',views.contact,name='contact'),
    path('blog',views.blog,name='blog'),
    path('blog/<int:pk>/', views.blog_single_display, name='blog_name_with_single'),
    path('single_listing',views.single_listing,name='single_listing'),
    path('single_blog',views.single_blog,name='single_blog'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT);
