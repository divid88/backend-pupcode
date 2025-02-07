from django.db import models

from core_apps.common.models import BaseModel


# Create your models here.
class Subject(BaseModel):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=300, null=True, blank=True)

    def __str__(self):
        return f'{self.title}'


class SubSubject(BaseModel):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE,
                                related_name='subs')
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=300, null=True, blank=True)

    def __str__(self):
        return f'{self.subject.title} -- {self.title}'

#
class Lesson(BaseModel):
    sub_subject = models.ForeignKey(SubSubject, on_delete=models.CASCADE,
                                    related_name='lessons')
    title = models.TextField(max_length=300, null=True, blank=True)
    describe = models.TextField(max_length=1000, null=None, blank=None)
    code = models.TextField(max_length=1000, null=None, blank=None)

    def __str__(self):
        return self.title
