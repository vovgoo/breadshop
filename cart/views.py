from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from catalog.models import Product, Category, Category_menu
from .cart import Cart
from .forms import CartAddProductForm, CartAddOneProduct


@require_POST
def cart_add(request, product_id):

    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    form_button = CartAddOneProduct(request.POST)
    if form_button.is_valid():
        cd = form_button.cleaned_data
        cart.add(product=product,
                 quantity=1,
                 update_quantity=cd['update'])

    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['Количество'],
                 update_quantity=cd['update'])
    return redirect('cart:cart_detail')

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect(request.META.get('HTTP_REFERER'))

def cart_detail(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart': cart,'title':'Bread | Корзина','category': category, 'categories': categories, 'products': products })

