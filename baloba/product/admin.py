from django.contrib import admin
from .models import Product, CartItem, Wishlist
from django.utils.html import format_html
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'value', 'image_of_product']
    def image_of_product(self, obj):
        if obj.product_image:
            img = '<img src="{url}/" height="60"'.format(url=obj.product_image.url)
            return format_html(img)
        return format_html("No Image")
    image_of_product.short_description = 'product image'

class CartItemAdmin(admin.ModelAdmin):
    list_display = ['product', 'quantity']
    
admin.site.register(Product, ProductAdmin)
admin.site.register(CartItem, CartItemAdmin)
admin.site.register(Wishlist)