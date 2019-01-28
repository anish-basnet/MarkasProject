from django.db import models

# Create your models here.\

class Realtor_Table(models.Model):
    realtor_name=models.CharField(max_length=100);
    realtor_image=models.ImageField();
    contact_no=models.DecimalField();
    mail_address=models.EmailField();
    description=models.CharField(max_length=2000);


class Property_Table(models.Model):
    property_heading=models.CharField(max_length=200);
    property_image=models.ImageField();
    city_located=models.CharField(max_length=100);
    full_address=models.CharField(max_length=200);
    status=models.CharField(max_length=100);
    num_bathroom=models.PositiveIntegerField();
    num_garage=models.PositiveIntegerField();
    tot_area_space=models.PositiveIntegerField();
    facilities=models.CharField(max_length=1000);
    published_date=models.DateTimeField();
    discount_offered=models.PositiveIntegerField();
    assign_to=models.ForeignKey(Realtor_Table,on_delete=models.CASCADE);

class Testimony_Table(models.Model):
    customer_name=models.CharField(max_length=100);
    customer_image=models.ImageField();
    heading=models.CharField(max_length=200);
    description=models.CharField(max_length=2000);

class Blog_Table(models.Model):
    published_by=models.CharField(max_length=100);
    published_date=models.DateTimeField();
    heading=models.CharField(max_length=200);
    description=models.CharField(max_length=4000);
    image=models.ImageField();

class Comment_Table(models.Model):
    comment_by=models.CharField(max_length=100);
    email=models.EmailField();
    date=models.DateTimeField();
    message=models.CharField(max_length=2000);
    to_blog=models.ForeignKey(Blog_Table,on_delete=models.CASCADE);