from django.contrib import admin

from .models import Subject, SubSubject, Lesson


admin.site.register(Subject)

class LessonAdmin(admin.StackedInline):
    model = Lesson

class SubSubjectAdmin(admin.ModelAdmin):
    inlines = [LessonAdmin]

admin.site.register(SubSubject, SubSubjectAdmin)
