# models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('teacher', 'Teacher'),
        ('student', 'Student'),
    )

    role = models.CharField(max_length=7, choices=ROLE_CHOICES, default='student')
    secret_word = models.CharField(max_length=20, blank=True, null=True)
    role_data = models.JSONField(default=dict, blank=True, null=True)

    def __str__(self):
        return self.username
