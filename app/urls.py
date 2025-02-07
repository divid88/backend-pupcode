
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
urlpatterns = [
    path('admin/', admin.site.urls),

    path("schema/", SpectacularAPIView.as_view(api_version="v1"), name="schema"),
    path("", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),

    path('api/v2/tutorial/', include('core_apps.tutorials.urls')),
    path('api/v2/exams/', include('core_apps.exams.urls')),
    path('api/v2/user/', include('core_apps.accounts.urls')),
    path('api/v2/auth/', include('core_apps.authenticate.urls')),
    path('api/v2/tutorials/', include('core_apps.tutorials.urls')),
    path('api/v2/codes/', include('core_apps.codes.urls')),

]
