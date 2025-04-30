from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import LessonSerializer,SubjectSerializer, SubSubjectSerializer, UserProgressSerializer
from .models import Subject, SubSubject, Lesson, UserProgress

class SubjectView(APIView):

    def get(self, request):
        subjects = Subject.objects.all()
        return Response(SubjectSerializer(subjects, many=True).data, status=200)


class SubSubjectView(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = [JWTAuthentication]

    def get(self, request, pk):
        sub_subjects = SubSubject.objects.filter(subject_id=pk).prefetch_related('lessons')
        return Response(SubSubjectSerializer(sub_subjects, many=True).data, status=200)


class UserProgressAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = [JWTAuthentication]

    def get(self, request):

        user = request.user
        try:
            user_progress = UserProgress.objects.filter(user=user, can_read=True)
        except ValueError:
            return Response()

        return Response(UserProgressSerializer(user_progress, many=True).data)