from django.urls import path

from . import views

urlpatterns = [
    path('subjects/', views.SubjectView.as_view(), name='subject_view'),
    path('subjects/<int:pk>/', views.SubSubjectView.as_view(), name='subject_detail_view'),
    path('user_progress/', views.UserProgressAPIView.as_view(), name='user_progress')
]