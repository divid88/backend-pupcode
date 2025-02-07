from django.contrib import admin

from .models import Code, SubCode, InputOutput


admin.site.register(Code)
admin.site.register(SubCode)
admin.site.register(InputOutput)
