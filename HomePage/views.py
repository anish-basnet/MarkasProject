from django.shortcuts import render
import datetime,random;
from .models import Contact_information_Submitted,Realtor_Table,Testimony_Table,Blog_Table,Comment_Table,Property_Table;

# Create your views here.
def main_index(request):
    property=Property_Table.objects.all();
    property=property[0:6];
    total=Realtor_Table.objects.all();
    testimony=Testimony_Table.objects.all();
    val=random.choice(total);
    overall_value=[];
    if(request.method=='POST'):
        keyword=request.POST['input'];
        city=request.POST['city'];
        catagory=request.POST['catagory'];
        discount=request.POST['discount'];
        garage=request.POST['garage'];
        bathroom=request.POST['bathroom'];


        if(city=="All Cities"):
            city="";
        if ( (catagory == "All Catagories")):
            catagory="";
        if ((discount == "All Offers")):
            discount=0;
        if ( (garage == "Garage")):
            garage=0;
        if ( (bathroom == "Bathrooms")):
            bathroom=0;
        overall_value=Property_Table.objects.filter(property_heading__startswith=keyword,city_located__startswith=city,status__startswith=catagory,discount_offered__gte=discount
                                                    ,num_garage__gte=garage,num_bathroom__gte=bathroom);

        return render(request,'listings.html',context={'property_list':overall_value})
    return render(request,'index.html',context={'selected_realtor':val,'testimony_list':testimony,'property_list':property});



def about_us(request):
    val=Realtor_Table.objects.all();
    property = Property_Table.objects.all();
    property = property[0:6];
    if (request.method == 'POST'):
        keyword = request.POST['input'];
        city = request.POST['city'];
        catagory = request.POST['catagory'];
        discount = request.POST['discount'];
        garage = request.POST['garage'];
        bathroom = request.POST['bathroom'];

        if (city == "All Cities"):
            city = "";
        if ((catagory == "All Catagories")):
            catagory = "";
        if ((discount == "All Offers")):
            discount = 0;
        if ((garage == "Garage")):
            garage = 0;
        if ((bathroom == "Bathrooms")):
            bathroom = 0;
        overall_value = Property_Table.objects.filter(property_heading__startswith=keyword,
                                                      city_located__startswith=city, status__startswith=catagory,
                                                      discount_offered__gte=discount
                                                      , num_garage__gte=garage, num_bathroom__gte=bathroom);

        return render(request, 'listings.html', context={'property_list': overall_value})
    return render(request,'about-us.html',context={'realtor_list':val,'property_list':property});

def listing(request):
    property = Property_Table.objects.all();
    if (request.method == 'POST'):
        keyword = request.POST['input'];
        city = request.POST['city'];
        catagory = request.POST['catagory'];
        discount = request.POST['discount'];
        garage = request.POST['garage'];
        bathroom = request.POST['bathroom'];

        if (city == "All Cities"):
            city = "";
        if ((catagory == "All Catagories")):
            catagory = "";
        if ((discount == "All Offers")):
            discount = 0;
        if ((garage == "Garage")):
            garage = 0;
        if ((bathroom == "Bathrooms")):
            bathroom = 0;
        overall_value = Property_Table.objects.filter(property_heading__startswith=keyword,
                                                      city_located__startswith=city, status__startswith=catagory,
                                                      discount_offered__gte=discount
                                                      , num_garage__gte=garage, num_bathroom__gte=bathroom);

        return render(request, 'listings.html', context={'property_list': overall_value})
    return render(request,'listings.html',context={'property_list':property});

def contact(request):
    if (request.method == 'POST'):
        name = request.POST['text'];
        number = request.POST['number'];
        emailll = request.POST['email'];
        messageee = request.POST['message'];
        con=Contact_information_Submitted(contact_name=name,phone_no=number,email=emailll,message=messageee,submitted_date=datetime.datetime.now());
        con.save();
    return render(request,'contact.html');

def blog(request):
    property = Property_Table.objects.all();
    property = property[0:6];
    blg=Blog_Table.objects.all();
    for x in blg:
        if(x.description.__len__()<=500):
            x.description=x.description;
        else:
            x.description=x.description[0:500];
    return render(request,'blog.html',context={'blog_list':blg,'property_list':property});

def blog_single_display(request,pk):
    full_blg=Blog_Table.objects.get(pk=pk);
    comment=Comment_Table.objects.filter(to_blog=pk);
    if(request.method == 'POST'):
        name = request.POST['nam'];
        message=request.POST['message'];
        email=request.POST['email'];
        conn=Comment_Table(comment_by=name,email=email,date=datetime.datetime.now(),message=message,to_blog=full_blg);
        conn.save();
    return render(request,'single-blog.html',context={'single_blog':full_blg,'comment':comment});

def single_listing(request):
    return render(request,'single-listings.html');

def single_blog(request):
    return render(request,'single-blog.html');

