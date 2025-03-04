from django.contrib import admin

from .models import CustomUser, OPTCode


admin.site.register(CustomUser)
admin.site.register(OPTCode)
