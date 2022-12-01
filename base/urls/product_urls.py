from django.urls import path

from base.views.product_views import get_product_details, get_products

urlpatterns = [
    path('', get_products, name='products'),
    path('/<str:pid>', get_product_details, name='product_details'),
]
