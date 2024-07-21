from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('register/role-specific/', views.role_specific_register, name='role-specific-register'),
    path('login/', views.login, name='login'),
    path('dashboard/teacher/', views.teacher_dashboard, name='teacher-dashboard'),
    path('dashboard/student/', views.student_dashboard, name='student-dashboard'),
]
