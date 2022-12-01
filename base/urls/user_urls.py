from django.urls import path

from base.views.user_views import MyTokenObtainPairView, get_user_profile, get_users, register_user

urlpatterns = [
    path('users/login', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/user', get_user_profile, name='user profile'),
    path('users', get_users, name="users"),
    path('users/register', register_user, name="register user")
]
