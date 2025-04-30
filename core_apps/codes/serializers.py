from rest_framework import  serializers

from .models import Code, SubCode, AnswerUser, InputOutput
from core_apps.tutorials.serializers import SubjectSerializer


class InputOutputSerializer(serializers.ModelSerializer):

    class Meta:
        model = InputOutput
        fields = ('id','sub_code', 'input', 'output')


class SubCodeSerializer(serializers.ModelSerializer):
    io = InputOutputSerializer(many=True, read_only=True)
    class Meta:
        model = SubCode
        fields = ('id', 'code', 'title', 'description', 'test_code', 'io')


class AnswerUserSerializer(serializers.ModelSerializer):
    sub_code = SubCodeSerializer(required=False)
    class Meta:
        model = AnswerUser
        fields = (
            'sub_code',
            'is_correct',
            'user_code')

class UserCodeSerializer(serializers.Serializer):
    user_code = serializers.FileField()


class CodeSerializer(serializers.ModelSerializer):
    subject = SubjectSerializer()
    sub_codes = SubCodeSerializer(many=True, read_only=True)
    class Meta:
        model = Code
        fields = ['id', 'subject', 'sub_codes']

