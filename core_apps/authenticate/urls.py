from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,  # For login
    TokenRefreshView,  # For refreshing token
    TokenVerifyView,  # Optional: For verifying token if needed
)

urlpatterns = [
    # Token endpoints for JWTs
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Login
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Refresh
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),  # Optional: Verification
]