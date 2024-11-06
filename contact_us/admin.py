from django.contrib import admin
from .models import ContactUs

# Register your models here.
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'problem','created_at']

    
admin.site.register(ContactUs, ContactModelAdmin)

