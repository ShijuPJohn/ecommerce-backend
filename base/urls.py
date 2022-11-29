from django.urls import path

from base.views import get_products, get_routes, get_product_details, MyTokenObtainPairView, get_user_profile

urlpatterns = [
    path('', get_routes, name='routes'),
    path('products', get_products, name='products'),
    path('products/<str:pid>', get_product_details, name='product_details'),
    path('users/login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/user', get_user_profile, name='user profile')

]
