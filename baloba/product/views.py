from django.shortcuts import render, get_object_or_404, redirect

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from product.models import Product, CartItem
# Create your views here.

def shop(request):
    
    items_list = Product.objects.all()
    paginator = Paginator(items_list, 4)

    page = request.GET.get('page')
    try:
        all_product = paginator.page(page)
    except PageNotAnInteger:
        all_product = paginator.page(1)
    except EmptyPage:
        all_product = paginator.page(paginator.num_pages)

    return render(request, 'shop.html', {
        'all_products': all_product,
        })
    
    # all_products = Product.objects.order_by('-id')
    # return render(request, 'shop.html', {'all_products': all_products})

def single_product(request, pk):
    all_product = Product.objects.order_by('-id')[:4]
    random_products = Product.objects.order_by('name')[:8]
    product_detail = get_object_or_404(Product, pk=pk)
    return render(request, 'single-product.html', {
        'product_detail': product_detail,
        'all_products': all_product,
        'random_products': random_products,
        })

def add_to_cart(request, product_id):
    product = Product.objects.get(pk=product_id)

    cart_item, created = CartItem.objects.get_or_create(
        product=product,
        defaults={'quantity': 1}
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('shopping_cart')  


