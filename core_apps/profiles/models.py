from django.db import models
from django.contrib.auth import get_user_model
from core_apps.common.models import BaseModel


User = get_user_model()

class Profile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    username = models.CharField(max_length=100, null=True, blank=True)
    bio = models.CharField(max_length=200, null=True, blank=True)
    level_user = models.IntegerField(default=1)
    score = models.IntegerField(default=0)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return f'{self.user.email} --- {self.username}'





