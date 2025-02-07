from rest_framework import serializers, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.validators import MinLengthValidator
from rest_framework_simplejwt.tokens import RefreshToken
from drf_spectacular.utils import extend_schema

from .models import CustomUser
from .validation import str_has_letter, str_has_special_char, str_has_number
from .services import register

from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)



class RegisterUser(APIView):
    
    class InputRegisterSerializer(serializers.Serializer):
        email = serializers.EmailField(max_length=200, required=False)
        
        password = serializers.CharField(validators=[
            str_has_number,
            str_has_letter,
            str_has_special_char,
            MinLengthValidator(limit_value=8)
        ])
        re_password = serializers.CharField(max_length=222)

    def validate_email(self, email):
        if CustomUser.objects.filter(email=email).exists():
            raise serializers.ValidationError('email already exist')
        return email
    
    def validate(self, data):
        if not data.get('password') or not data.get('re_password'):
            raise serializers.ValidationError("please fill password and confirm password")
        
        if data.get('password') != data.get('re_password'):
            raise serializers.ValidationError("confirm password must be equal to password")
        return data
    
    
    class OutputRegisterSerializer(serializers.ModelSerializer):
        token  = serializers.SerializerMethodField('get_token')
        
        class Meta:
            model = CustomUser
            fields = ['email','token', "created", "updated"]
            
        def get_token(self, user):
            data = dict()
            token_class = RefreshToken
            
            refresh = token_class.for_user(user)
            
            data['refresh'] = str(refresh)
            data['access'] = str(refresh.access_token)
            
            return data

    @extend_schema(request=InputRegisterSerializer, responses=OutputRegisterSerializer)
    def post(self, request):
        serializer_data = self.InputRegisterSerializer(data=request.data)
        
        serializer_data.is_valid(raise_exception=True)
        try:
            user = register(
                email=serializer_data.validated_data.get('email'),
                password=serializer_data.validated_data.get('password')
            )
        except Exception as ex:
            return Response(f'Database error {ex}', status=status.HTTP_400_BAD_REQUEST)

        return Response(self.OutputRegisterSerializer(user, 
                                                      context={'request':request}).data,
                        status=status.HTTP_201_CREATED)


class CustomTokenObtainPairView(TokenObtainPairView):

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)

        if response.status_code == 200:
            access_token = response.data.get('access')
            refresh_token = response.data.get('refresh')

            response.set_cookie(
                'access', access_token,
                max_age=settings.AUTH_COOKIE_ACCESS_MAX_AGE,
                path = '/',
                secure=True,
                httponly=True,
                samesite=settings.AUTH_COOKIE_SAMESITE
            )

            response.set_cookie(
                'refresh', refresh_token,
                max_age=settings.AUTH_COOKIE_REFRESH_MAX_AGE ,
                path = settings.AUTH_COOKIE_PATH,
                secure=settings.AUTH_COOKIE_SECURE,
                httponly=settings.AUTH_COOKIE_HTTP_ONLY,
                samesite=settings.AUTH_COOKIE_SAMESITE
            )
        return response


class CustomTokenRefreshView(TokenRefreshView):
    def post(self, request, *args, **kwargs):
        refresh_token =  request.COOKIES.get('refresh')

        if refresh_token:
            request.data['refresh'] = refresh_token

        response = super().post(request, *args, **kwargs)

        if response.status_code == 200:
            access_token = response.data.get('access')
            response.set_cookie(
                'access', access_token,
                max_age=settings.AUTH_COOKIE_ACCESS_MAX_AGE,
                path = settings.AUTH_COOKIE_PATH,
                secure=settings.AUTH_COOKIE_SECURE,
                httponly=settings.AUTH_COOKIE_HTTP_ONLY,
                samesite=settings.AUTH_COOKIE_SAMESITE
            )
        return response


class CustomTokenVerifyView(TokenVerifyView):
    def post(self, request, *args, **kwargs):
        access_token =  request.COOKIES.get('access')

        if access_token:
            request.data['token'] = access_token

        response = super().post(request, *args, **kwargs)


class LogoutAPIView(APIView):
    def post(self, request, *args, **kwargs):
        response  = Response(status=status.HTTP_204_NO_CONTENT)
        response.delete_cookie('access')
        response.delete_cookie('refresh')

        return response