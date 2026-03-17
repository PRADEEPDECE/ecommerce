
from django.shortcuts import render, redirect
from .models import Product, CartItem

def product_list(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})

def cart_view(request):
    items = CartItem.objects.all()
    total = sum(item.product.price * item.quantity for item in items)
    return render(request, 'cart.html', {'items': items, 'total': total})

def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    item, created = CartItem.objects.get_or_create(product=product)
    if not created:
        item.quantity += 1
    item.save()
    return redirect('cart')

def remove_from_cart(request, item_id):
    item = CartItem.objects.get(id=item_id)
    item.delete()
    return redirect('cart')

def update_quantity(request, item_id, action):
    item = CartItem.objects.get(id=item_id)
    if action == 'increase':
        item.quantity += 1
    elif action == 'decrease' and item.quantity > 1:
        item.quantity -= 1
    item.save()
    return redirect('cart')
