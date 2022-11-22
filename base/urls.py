from django.urls import path

from base.views import get_products, get_routes, get_product_details

urlpatterns = [
    path('', get_routes, name='routes'),
    path('products', get_products, name='products'),
    path('product/<str:pid>', get_product_details, name='product_details'),

]
