from django.contrib import admin

from .models import ContactUsModel, Subscriber

# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']
    list_filter = ['email']

admin.site.register(ContactUsModel, ContactAdmin)
@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = (['email'])
    list_filter =  (['email'])
    search_fields = (['email'])