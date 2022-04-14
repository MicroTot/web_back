import imp
from django.contrib import admin
from main.models import * 

# Register your models here.
admin.site.register(User_Category)
admin.site.register(Jobs)
admin.site.site_header  =  "Strathmore Graduate Job-Finder" 