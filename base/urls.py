from django.urls import path

from base.views import get_products, get_routes, get_products_details

urlpatterns = [
    path('', get_routes, name='routes'),
    path('products', get_products, name='products'),
    path('products/<str:pid>', get_products_details, name='product_details'),

]
