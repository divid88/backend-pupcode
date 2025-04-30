from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

from core_apps.profiles.models import Profile
from core_apps.tutorials.models import UserProgress, Subject


User = get_user_model()

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance, username=instance.email.split('@')[0])
        subject = Subject.objects.get(pk=1)

        user_progress = UserProgress.objects.create(user=instance, subject=subject)
        user_progress.can_read = True
        user_progress.save()