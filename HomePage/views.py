from django.shortcuts import render

# Create your views here.
def main_index(request):
    return render(request,'index.html');


def about_us(request):
    return render(request,'about-us.html');

def listing(request):
    return render(request,'listings.html');

def contact(request):
    return render(request,'contact.html');

def blog(request):
    return render(request,'blog.html');

def single_listing(request):
    return render(request,'single-listings.html');

def single_blog(request):
    return render(request,'single-blog.html');