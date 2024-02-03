from django.db import models
from baloba.utils.base import BaseModel
# Create your models here.

class Product(BaseModel):
    name = models.CharField(max_length=100, verbose_name='Name of product', help_text='Maximum 100 characters')
    star = models.IntegerField(verbose_name='Star of product')
    value = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Value of product')
    description = models.TextField(verbose_name='Description of product', null=False, blank=True)
    brand = models.CharField(max_length=50, verbose_name='Brand', help_text='Maximum 50 characters')
    product_code = models.CharField(max_length=20, verbose_name='Product Code', help_text='Maximum 20 characters')
    reward_points = models.IntegerField(verbose_name='Reward Points of product')
    availability = models.BooleanField(default=True, verbose_name='Availability of product')
    product_image = models.ImageField(upload_to='product/product_image', verbose_name="product_image'", null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'All Product'

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    
class Wishlist(models.Model):
    products = models.ManyToManyField(Product)

    def add_to_wishlist(self, product):
        self.products.add(product)
        