from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import LessonSerializer,SubjectSerializer, SubSubjectSerializer
from .models import Subject, SubSubject, Lesson

class SubjectView(APIView):

    def get(self, request):
        subjects = Subject.objects.all()

        return Response(SubjectSerializer(subjects, many=True).data, status=200)


class SubSubjectView(APIView):
    def get(self, request, pk):
        sub_subjects = SubSubject.objects.filter(subject_id=pk).prefetch_related('lessons')
        return Response(SubSubjectSerializer(sub_subjects, many=True).data, status=200)