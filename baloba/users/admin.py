from django.contrib import admin
from .models import User, UserProfile
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email']
    list_filter = ['email']

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user','user_type', 'about']
    
admin.site.register(User, UserAdmin)
admin.site.register(UserProfile, UserProfileAdmin)