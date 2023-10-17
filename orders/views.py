from django.shortcuts import render, get_object_or_404
from .models import OrderItem
from .forms import OrderCreateForm
from catalog.models import Category, Product, Category_menu
from cart.cart import Cart


def order_create(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order, product=item['product'], price=item['price'], quantity=item['quantity'])
            cart.clear()
            return render(request, 'orders/checkout_create.html', {'order': order, 'category': category, 'categories': categories, 'products': products,})
    else:
        form = OrderCreateForm
    return render(request, 'orders/checkout.html', {'cart': cart,'category': category, 'categories': categories, 'products': products, 'form': form})