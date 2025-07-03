from django.contrib import admin
from .models import Restaurant,MenuItem, Contact_Query
# Register your models here.
admin.site.register(Restaurant)
admin.site.register(MenuItem)
admin.site.register(Contact_Query)