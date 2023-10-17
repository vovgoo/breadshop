from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.index, name='home'),
    path('store', views.product_list, name='store'),
    path('store/<category_slug>/', views.product_list, name='product_list_by_category'),
    path('store/<id>/<slug>/', views.product_detail, name='product_detail'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)