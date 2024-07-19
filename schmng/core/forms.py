from django import forms
from django.core.exceptions import ValidationError
from .models import Teacher, Student, User  # Import the custom User model

class UserRegisterForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password', 'class': 'form-control'}))
    role = forms.ChoiceField(choices=[('teacher', 'Teacher'), ('student', 'Student')], widget=forms.RadioSelect(attrs={'class': 'form-radio'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'role']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'form-control'}),
        }

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords do not match")
        return password2

class TeacherRegisterForm(forms.ModelForm):
    secret_word = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Secret Word', 'class': 'form-control'}))

    class Meta:
        model = Teacher
        fields = ['secret_word']
        widgets = {
            'secret_word': forms.PasswordInput(attrs={'placeholder': 'Secret Word', 'class': 'form-control'}),
        }

    def clean_secret_word(self):
        secret_word = self.cleaned_data.get("secret_word")
        if secret_word != 'teach':
            raise ValidationError("Invalid secret word")
        return secret_word

class StudentRegisterForm(forms.ModelForm):
    secret_word = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Secret Word', 'class': 'form-control'}))

    class Meta:
        model = Student
        fields = ['secret_word']
        widgets = {
            'secret_word': forms.PasswordInput(attrs={'placeholder': 'Secret Word', 'class': 'form-control'}),
        }

    def clean_secret_word(self):
        secret_word = self.cleaned_data.get("secret_word")
        if secret_word != 'learn':
            raise ValidationError("Invalid secret word")
        return secret_word
