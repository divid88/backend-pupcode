from rest_framework import serializers

from .models import Subject, SubSubject, Lesson


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ('id', 'title', 'describe', 'code')


class SubSubjectSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True, read_only=True)
    class Meta:
        model = SubSubject
        fields = ('id', 'title', 'description', 'lessons')


class SubjectSerializer(serializers.ModelSerializer):
    sub_subjects = SubSubjectSerializer(many=True, read_only=True)
    class Meta:
        model = Subject
        fields = ('id', 'title', 'description', 'sub_subjects')