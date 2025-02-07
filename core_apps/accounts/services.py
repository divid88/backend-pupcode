from .models import CustomUser
from django.db import transaction


def create_user(*, email ,password):
    return CustomUser.objects.create_user( 
                                   email=email, 
                                   password=password,
                                   
                                   )

@transaction.atomic
def register(*,email, password):
    user = create_user(email=email, password=password)
    return user