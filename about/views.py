from django.shortcuts import render, get_object_or_404
from catalog.models import Category, Product, Category_menu
from cart.cart import Cart

def about(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    cart = Cart(request)
    return render(request, 'about/information.html', {'title':'Bread | Информация','cart': cart,'category': category, 'categories': categories, 'products': products})

