from django.http import JsonResponse

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

from base.models import Product
from base.serializers import ProductSerializer


@api_view(['GET'])
def get_routes(request):
    return Response('/api/products')


@api_view(['GET'])
def get_products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_product_details(request, pid):
    product = Product.objects.get(pk=pid)
    serializer = ProductSerializer(product)
    return Response(serializer.data)
