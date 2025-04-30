from django.db import models
from django.contrib.auth import  get_user_model

from core_apps.common.models import BaseModel

User = get_user_model()

# Create your models here.
class Subject(BaseModel):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=300, null=True, blank=True)
    need_score = models.PositiveSmallIntegerField(default=10)

    def __str__(self):
        return f'{self.title}'


class UserProgress(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)  # آیا موضوع کامل شده؟
    completed_at = models.DateTimeField(null=True, blank=True)  # زمان تکمیل
    can_read = models.BooleanField(default=False)

    class Meta:
        unique_together = ('user', 'subject')  # هر کاربر برای هر موضوع فقط یک پیشرفت داره

    def __str__(self):
        return f"{self.user.email} - {self.subject.title}"

    def check_can_read(self):
        if self.user.profile.score > self.subject.need_score:
            self.can_read = True


class SubSubject(BaseModel):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE,
                                related_name='subs')
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=300, null=True, blank=True)

    def __str__(self):
        return f'{self.subject.title} -- {self.title}'


class Lesson(BaseModel):
    sub_subject = models.ForeignKey(SubSubject, on_delete=models.CASCADE,
                                    related_name='lessons')
    title = models.TextField(max_length=300, null=True, blank=True)
    describe = models.TextField(max_length=1000, null=None, blank=None)
    code = models.TextField(max_length=1000, null=None, blank=None)

    def __str__(self):
        return self.title
