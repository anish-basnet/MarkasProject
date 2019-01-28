from django.contrib import admin
from .models import Realtor_Table,Property_Table,Testimony_Table,Blog_Table,Comment_Table;

# Register your models here.

admin.site.register(Realtor_Table);
admin.site.register(Property_Table);
admin.site.register(Testimony_Table);
admin.site.register(Blog_Table);
admin.site.register(Comment_Table);