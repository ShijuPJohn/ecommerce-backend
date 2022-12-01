from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
# Create your views here.
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView

from base.models import Product
from base.serializers import ProductSerializer, MyTokenObtainPairSerializer, UserSerializer, UserSerializerWithToken


@api_view(['GET'])
def get_routes(request):
    return Response('/api/products')


@api_view(['GET'])
def get_products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAdminUser])
def get_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_product_details(request, pid):
    product = Product.objects.get(pk=pid)
    serializer = ProductSerializer(product)
    return Response(serializer.data)


@api_view(["POST"])
def register_user(request):
    data = request.data
    user = User.objects.create(
        first_name=data["first_name"],
        username=data["email"],
        email=data["email"],
        password=make_password(data["password"]),
    )
    serializer = UserSerializerWithToken(user)

    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_profile(request):
    user = request.user
    serializer = UserSerializer(user)
    return Response(serializer.data)


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
