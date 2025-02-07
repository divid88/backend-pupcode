from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import InputOutputSerializer, CodeSerializer, SubCodeSerializer, AnswerUserSerializer
from .models import InputOutput, Code, SubCode, AnswerUser


class AllCodeSubject(APIView):
    def get(self, request, subject_id):
        codes = Code.objects.filter(subject_id=subject_id).prefetch_related('sub_codes')
        return Response(CodeSerializer(codes, many=True).data, status=200)


class SubCodeView(APIView):
    def get(self, request, sub_code_id):
        sub_code = SubCode.objects.get(id=sub_code_id)
        return Response(SubCodeSerializer(sub_code).data, status=200)