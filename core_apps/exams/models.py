from django.db import models

from core_apps.common.models import BaseModel
from core_apps.tutorials.models import Subject


class Exam(BaseModel):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE,
                                related_name='exams')
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.title

class Questions(BaseModel):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE,
                             related_name='questions')
    text = models.TextField()

    def __str__(self):
        return self.text


class Options(BaseModel):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE,
                                 related_name='options')
    text = models.TextField()
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text


class Results(BaseModel):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE,
                             related_name='results')
    user = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE,
                             related_name='results')
    score = models.IntegerField()

    def __str__(self):
        return f"{self.user.username} - {self.exam.title} - {self.score}"
