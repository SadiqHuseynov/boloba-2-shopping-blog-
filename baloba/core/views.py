from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactUsForm
from .models import ContactUsModel
from blog.models import Blogs
from product.models import Product, CartItem
from django.contrib import messages

# Create your views here.


def index(request):
    blogs = Blogs.objects.filter(is_check=True).order_by('-id')[:4]
    products = Product.objects.order_by('-id')[:8]
    featured_p = Product.objects.order_by('name')
    best_s = Product.objects.all()[:4]
    
    cart_items = CartItem.objects.all()
    total_price = sum(item.product.value * item.quantity for item in cart_items)
    return render(request, 'main.html', {
        'blogs': blogs,
        'products': products,
        'featured': featured_p,
        'best_s': best_s,
        'cart_items': cart_items,
        'total_price': total_price,
        })

def search_product(request):
    if request.method == 'POST':
        query = request.POST.get('search', '')
        products = Product.objects.filter(name__icontains=query)
    else:
        products = Product.objects.all()

    return render(request, 'search.html', {'products': products})

def contact_us(request):
    if request.POST.get('name'):
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        success = ContactUsModel(name=name, email=email, message=message)
        success.save()
        messages.success(request, 'Your message has been sended!')
    return render(request, 'contact-us.html',{'form': ContactUsForm})
