from django.urls import path

from . import views

urlpatterns = [
    path('subject/<int:subject_id>/', views.AllCodeSubject.as_view(), name='code_view'),
    path('sub_code/<int:sub_code_id>/', views.SubCodeView.as_view(), name='sub_code_view'),
    path('test_code/<int:pk>/', views.TestUserCode.as_view(), name='test_user_code'),
]