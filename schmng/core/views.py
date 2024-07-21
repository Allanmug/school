from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, RoleSpecificForm
from datetime import datetime

def home(request):
    current_date = datetime.now()
    return render(request, 'core/home.html', {'current_date': current_date})

def register(request):
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data["password1"])
            user.save()
            
            # Log the user in after saving the user
            auth_login(request, user)
            
            return redirect('role-specific-register')
    else:
        user_form = UserRegisterForm()
    return render(request, 'core/register.html', {'user_form': user_form})

@login_required
def role_specific_register(request):
    if request.method == 'POST':
        form = RoleSpecificForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            request.user.save()
            return redirect('login')
    else:
        form = RoleSpecificForm(instance=request.user)
    
    if request.user.role == 'teacher':
        template_name = 'core/teacher_register.html'
    else:
        template_name = 'core/student_register.html'
    
    return render(request, template_name, {'form': form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            if user.role == 'teacher':
                return redirect('teacher-dashboard')
            elif user.role == 'student':
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
