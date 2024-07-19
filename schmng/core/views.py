from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, TeacherRegisterForm, StudentRegisterForm
from datetime import datetime

def home(request):
    current_date = datetime.now()
    return render(request, 'core/home.html', {'current_date': current_date})

def register(request):
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            role = user_form.cleaned_data.get('role')
            user.save()
            
            # Log the user in after saving the user
            auth_login(request, user)
            
            if role == 'teacher':
                return redirect('teacher-register')
            elif role == 'student':
                return redirect('student-register')
    else:
        user_form = UserRegisterForm()
    return render(request, 'core/register.html', {'user_form': user_form})

@login_required
def teacher_register(request):
    if request.method == 'POST':
        form = TeacherRegisterForm(request.POST)
        if form.is_valid():
            teacher = form.save(commit=False)
            teacher.user = request.user
            teacher.save()
            request.user.is_teacher = True
            request.user.save()
            return redirect('login')
    else:
        form = TeacherRegisterForm()
    return render(request, 'core/teacher_register.html', {'form': form})

@login_required
def student_register(request):
    if request.method == 'POST':
        form = StudentRegisterForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.user = request.user
            student.save()
            request.user.is_student = True
            request.user.save()
            return redirect('login')
    else:
        form = StudentRegisterForm()
    return render(request, 'core/student_register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            if user.is_teacher:
                return redirect('teacher-dashboard')
            elif user.is_student:
                return redirect('student-dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'core/login.html', {'form': form})

@login_required
def teacher_dashboard(request):
    return render(request, 'core/teacher_dashboard.html', {'user': request.user})

@login_required
def student_dashboard(request):
    return render(request, 'core/student_dashboard.html', {'user': request.user})
