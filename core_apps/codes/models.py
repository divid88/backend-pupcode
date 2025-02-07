from django.db import models
from django.contrib.auth import get_user_model

from core_apps.common.models import BaseModel
from core_apps.tutorials.models import Subject

User = get_user_model()


class Code(BaseModel):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='codes')

    def __str__(self):
        return self.subject.title


class SubCode(BaseModel):
    code = models.ForeignKey(Code, on_delete=models.CASCADE, related_name='sub_codes')
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=300, null=True, blank=True)
    test_code = models.FileField()

    def __str__(self):
        return f'{self.code.subject.title} --- {self.title}  '


class AnswerUser(BaseModel):
    sub_code = models.OneToOneField(SubCode, on_delete=models.CASCADE, related_name='answers_user')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='answers')
    is_correct = models.BooleanField(default=False)
    user_code = models.FileField()

    def __str__(self):
       return f'{self.sub_code.title} --- {self.user.username}'


class InputOutput(BaseModel):
    sub_code = models.ForeignKey(SubCode, on_delete=models.CASCADE, related_name='io')
    input = models.TextField()
    output = models.TextField()

    def __str__(self):
        return f'{self.sub_code.title}'