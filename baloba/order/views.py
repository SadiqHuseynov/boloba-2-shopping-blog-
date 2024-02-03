from django.shortcuts import render, get_object_or_404, redirect
from product.models import CartItem, Product, Wishlist
# Create your views here.

def shopping_cart(request):
    cart_items = CartItem.objects.all()
    total_price = sum(item.product.value * item.quantity for item in cart_items)
    
    return render(request, 'shopping-cart.html', {'cart_items': cart_items, 'total_price': total_price})

def delete_cart_item(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    cart_item.delete()
    return redirect('shopping_cart') 

def wishlist(request):
    user_wishlist, created = Wishlist.objects.get_or_create()
    wishlist_products = user_wishlist.products.all()
    return render(request, 'wishlist.html', {'wishlist_products': wishlist_products})

def add_to_wish_list(request, product_id):
    product = Product.objects.get(id=product_id)
    user_wishlist, created = Wishlist.objects.get_or_create()
    user_wishlist.add_to_wishlist(product)
    return redirect('wishlist')

def checkout(request):
    return render(request, 'checkout.html')


