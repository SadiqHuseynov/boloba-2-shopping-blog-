from django.contrib import admin
from .models import *
from django.utils.html import format_html
# Register your models here.
admin.site.site_header = 'Baloba Admin Panel'
admin.site.site_title = 'Baloba 2'

class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'is_check', 'poster_of_blog']
    list_filter = ['blog_category','tag_name', 'is_check']
    
    def poster_of_blog(self, obj):
        if obj.poster:
            img = '<img src="{url}/" height="60"'.format(url=obj.poster.url)
            return format_html(img)
        return format_html("No Poster")
    poster_of_blog.short_description = 'Poster'

admin.site.register(Blogs, BlogAdmin)
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Tags)