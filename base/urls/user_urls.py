from django.urls import path

from base.views.user_views import *

urlpatterns = [
    path('/login', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('/user', get_user_profile, name='user profile'),
    path('', get_users, name="users"),
    path('/register', register_user, name="register user")
]
