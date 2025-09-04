from django.urls import path
from .views import RegisterView, ForgotPasswordView, UserProfileAPIView, LogoutView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
     path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("forgot-password/", ForgotPasswordView.as_view(), name="forgot-password"),
     path('profile/', UserProfileAPIView.as_view(), name='profile'),
      path('logout/', LogoutView.as_view(), name='logout'),
    
]
