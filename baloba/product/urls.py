from django.urls import path

from . import views

urlpatterns = [
    path('shop/', views.shop, name="shop"),
    path('single_product/<int:pk>/', views.single_product, name="single_product"),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
]
 