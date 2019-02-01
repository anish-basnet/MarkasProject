from django.db import models

# Create your models here.\

class Realtor_Table(models.Model):
    realtor_name=models.CharField(max_length=100);
    realtor_image=models.ImageField(upload_to='Realtor_image',blank=True);
    contact_no=models.CharField(max_length=50);
    mail_address=models.EmailField();
    description=models.TextField();

    def __str__(self):
        return self.realtor_name


class Property_Table(models.Model):
    property_heading=models.CharField(max_length=200);
    property_image=models.ImageField();
    city_located=models.CharField(max_length=100);
    full_address=models.CharField(max_length=200);
    status=models.CharField(max_length=100);
    price=models.BigIntegerField();
    num_bathroom=models.PositiveIntegerField();
    num_garage=models.PositiveIntegerField();
    tot_area_space=models.PositiveIntegerField();
    facilities=models.CharField(max_length=1000);
    published_date=models.DateTimeField();
    discount_offered=models.PositiveIntegerField();
    assign_to=models.ForeignKey(Realtor_Table,on_delete=models.CASCADE);

    def __str__(self):
        return self.property_heading

class Testimony_Table(models.Model):
    customer_name=models.CharField(max_length=100);
    customer_image=models.ImageField();
    heading=models.CharField(max_length=200);
    description=models.TextField();

    def __str__(self):
        return self.customer_name

class Blog_Table(models.Model):
    published_by=models.CharField(max_length=100);
    published_date=models.DateTimeField();
    heading=models.CharField(max_length=200);
    description=models.TextField();
    image=models.ImageField();

    def __str__(self):
        return self.published_by

class Comment_Table(models.Model):
    comment_by=models.CharField(max_length=100);
    email=models.EmailField();
    date=models.DateTimeField();
    message=models.TextField();
    to_blog=models.ForeignKey(Blog_Table,on_delete=models.CASCADE);

    def __str__(self):
        return self.comment_by

class Contact_information_Submitted(models.Model):
    contact_name=models.CharField(max_length=100);
    phone_no=models.CharField(max_length=50);
    email=models.EmailField();
    message=models.TextField();
    submitted_date=models.DateTimeField();

    def __str__(self):
        return self.contact_name;