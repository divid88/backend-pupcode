from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from .views import (RegisterUser, ActiveUserAPIView, CustomTokenRefreshView, CustomTokenObtainPairView,
                    SendEmailAPIView, ChangePasswordAPIView)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
    path('token/', CustomTokenObtainPairView.as_view(), name='token_verify'),

    path('api/register/', RegisterUser.as_view(), name='register_view'),
    path('active/user', ActiveUserAPIView.as_view(), name='active_user'),
    path('send-email/', SendEmailAPIView.as_view(), name='send_email'),
    path('change-password/', ChangePasswordAPIView.as_view(), name='change_password'),
]