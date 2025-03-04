from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from random import randint

from core_apps.common.models import BaseModel


class CustomUserManager(BaseUserManager):
    
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        user = self.model(
            email=self.normalize_email(email.lower())
        )

        if password is not None:
            user.set_password(password)

        else:
            user.set_unusable_password()

        user.full_clean()
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None):
        user = self.create_user(email=email, password=password)
        
        if user:
            user.is_active = True
            user.is_staff = True
            user.is_admin = True
            user.is_superuser = True
            user.save(using=self._db)
            return user
        
        
class CustomUser(BaseModel, AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
     
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'


class OPTCode(BaseModel):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="opt")
    code = models.CharField(max_length=6, default=randint(100000, 999999))


    def __str__(self):
        return self.code


