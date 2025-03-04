
# urls.py
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import LogoutView, UserDetailView

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/logout/', LogoutView.as_view(), name='logout'),
    path('api/user/', UserDetailView.as_view(), name='user_detail'),
]





# from django.urls import path
# from .views import LoginView, LogoutView, RefreshTokenView
#
#
# urlpatterns = [
#     path('login/', LoginView.as_view(), name='login'),
#     path('logout/', LogoutView.as_view(), name='logout'),
#     path('token/refresh/', RefreshTokenView.as_view(), name='token_refresh'),
# ]
