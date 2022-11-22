from django.http import JsonResponse

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

from base.products import products


@api_view(['GET'])
def get_routes(request):
    return Response('/api/products')


@api_view(['GET'])
def get_products(request):
    return Response(products)


@api_view(['GET'])
def get_products_details(request, pid):
    product = list(filter((lambda a: a['_id'] == pid), products))[0]
    print(product)
    return Response(product)
