from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView

from base.models import Product
from base.serializers import ProductSerializer, MyTokenObtainPairSerializer, UserSerializer, UserSerializerWithToken


@api_view(['GET'])
def get_routes(request):
    return Response('/api/products')



