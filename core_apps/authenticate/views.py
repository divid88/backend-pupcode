# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication


class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = [JWTAuthentication]

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class UserDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({
            "id": user.id,
            "email": user.email,
        })





# from django.contrib.auth import authenticate
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework_simplejwt.tokens import RefreshToken
# from rest_framework_simplejwt.views import TokenVerifyView
#
#
# class LoginView(APIView):
#     def post(self, request):
#         email = request.data.get("email")
#         password = request.data.get("password")
#         user = authenticate(email=email, password=password)
#
#         if user is not None:
#             refresh = RefreshToken.for_user(user)
#             response = Response({"message": "Login successful!"})
#             response.set_cookie(
#                 key="access_token",
#                 value=str(refresh.access_token),
#                 httponly=True,
#                 secure=True,
#                 # samesite="Lax",
#             )
#             response.set_cookie(
#                 key="refresh_token",
#                 value=str(refresh),
#                 httponly=True,
#                 secure=True,
#                 samesite="Lax",
#             )
#             return response
#
#         return Response({"error": "Invalid credentials"}, status=401)
#
#
# class LogoutView(APIView):
#     def post(self, request):
#         response = Response({"message": "Logged out"})
#         response.delete_cookie("access_token")
#         response.delete_cookie("refresh_token")
#         return response
#
#
# class RefreshTokenView(APIView):
#     def post(self, request):
#         refresh_token = request.COOKIES.get("refresh_token")
#         if refresh_token:
#             try:
#                 refresh = RefreshToken(refresh_token)
#                 access_token = str(refresh.access_token)
#                 response = Response({"message": "Token refreshed"})
#                 response.set_cookie(
#                     key="access_token",
#                     value=str(refresh.access_token),
#                     httponly=True,
#                     secure=True,
#                     samesite="Lax",
#                 )
#                 return response
#             except Exception:
#                 return Response({"error": "Invalid refresh token"}, status=401)
#         return Response({"error": "No refresh token"}, status=400)
#
#
#
# class CustomTokenVerifyView(TokenVerifyView):
#     def post(self, request, *args, **kwargs):
#         access_token = request.COOKIES.get('access_token')
#
#         if access_token:
#             request.data['token'] = access_token
#
#         return super().post(request, *args, **kwargs)
#
#
