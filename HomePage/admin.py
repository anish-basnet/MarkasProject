from django.contrib import admin
from .models import Realtor_Table,Property_Table,Testimony_Table,Blog_Table,Comment_Table,Contact_information_Submitted

# Register your models here.


class RealtorAdmin(admin.ModelAdmin):
    model=Realtor_Table;
    list_display = ('realtor_name','realtor_image','contact_no','mail_address')

class PropertyAdmin(admin.ModelAdmin):
    model=Property_Table;
    list_display = ('property_heading','full_address','status','assign_to','published_date');

class ContactAdmin(admin.ModelAdmin):
    model=Contact_information_Submitted;
    list_display = ('contact_name','phone_no','email','submitted_date');

class TestimonyAdmin(admin.ModelAdmin):
    model=Testimony_Table;
    list_display = ('customer_name','heading','customer_image');

class BlogAdmin(admin.ModelAdmin):
    model = Blog_Table;
    list_display = ('heading', 'published_by', 'published_date');

class CommentAdmin(admin.ModelAdmin):
    model = Comment_Table;
    list_display = ('comment_by', 'date', 'message','to_blog');

admin.site.register(Realtor_Table,RealtorAdmin);
admin.site.register(Property_Table,PropertyAdmin);
admin.site.register(Testimony_Table,TestimonyAdmin);
admin.site.register(Blog_Table,BlogAdmin);
admin.site.register(Comment_Table,CommentAdmin);
admin.site.register(Contact_information_Submitted,ContactAdmin);