from django.contrib import admin

from .models import Exam, Questions, Options, Results


admin.site.register(Exam)
admin.site.register(Questions)
admin.site.register(Options)
admin.site.register(Results)

