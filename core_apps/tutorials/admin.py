from django.contrib import admin

from .models import Subject, SubSubject, Lesson


class SubjectAdmin(admin.ModelAdmin):
    model = Subject
    list_display = ('id', 'title', 'description')

admin.site.register(Subject, SubjectAdmin)

class LessonAdmin(admin.StackedInline):
    model = Lesson

class SubSubjectAdmin(admin.ModelAdmin):
    inlines = [LessonAdmin]

admin.site.register(SubSubject, SubSubjectAdmin)
