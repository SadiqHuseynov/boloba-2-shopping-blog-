from django.urls import path

from . import views

urlpatterns = [
    path('shopping_cart/', views.shopping_cart, name="shopping_cart"),
    path('delete-cart-item/<int:item_id>/', views.delete_cart_item, name='delete_cart_item'),
    path('checkout/', views.checkout, name="checkout"),
    path('wishlist/', views.wishlist, name="wishlist"),
    path('add_to_wish_list/<int:product_id>/', views.add_to_wish_list, name='add_to_wish_list'),
]
 