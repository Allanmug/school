from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('register/teacher/', views.teacher_register, name='teacher-register'),
    path('register/student/', views.student_register, name='student-register'),
    path('login/', views.login, name='login'),
    path('dashboard/teacher/', views.teacher_dashboard, name='teacher-dashboard'),
    path('dashboard/student/', views.student_dashboard, name='student-dashboard'),
]
