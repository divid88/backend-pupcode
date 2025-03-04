from rest_framework import serializers

from .models import Profile


class ReadProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'username', 'bio', 'image', 'level_user', 'score')

