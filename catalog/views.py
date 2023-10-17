from django.shortcuts import render, get_object_or_404
from .models import Category, Product, Category_menu
from cart.forms import CartAddProductForm, CartAddOneProduct
from cart.cart import Cart



def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    cart = Cart(request)
    cart_product_form = CartAddOneProduct()
    return render(request, 'catalog/store.html', {'title':'Bread | Магазин','cart': cart,'category': category, 'categories': categories, 'products': products, "cart_product_form": cart_product_form})


def index(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    category_menu = Category_menu.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    cart = Cart(request)
    cart_product_form = CartAddOneProduct()
    return render(request, 'catalog/index.html', {"title": "Bread Shop","cart": cart, 'category': category, 'categories': categories,'products': products, 'category_menu': category_menu, "cart_product_form": cart_product_form})

def product_detail(request, id, slug, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    category_menu = Category_menu.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddOneProduct()
    cart_product_form_all = CartAddProductForm()
    cart = Cart(request)
    return render(request,'catalog/product.html', {"title": "Bread Shop", "cart": cart,'category': category, 'categories': categories,'products': products, 'category_menu': category_menu, "product": product, "cart_product_form": cart_product_form, "cart_product_form_all": cart_product_form_all})

