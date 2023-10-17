from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart/', include(("cart.urls", "cart"), namespace="cart")),
    path('orders/', include(("orders.urls", "orders"), namespace="orders")),
    path('about-us/', include(("about.urls", "about"), namespace="about")),
    path('', include(("catalog.urls", "catalog"), namespace="catalog")),
]


