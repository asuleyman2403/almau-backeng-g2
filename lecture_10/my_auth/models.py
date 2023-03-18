from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from datetime import datetime


class User(AbstractUser, PermissionsMixin):
    email = models.EmailField(null=False, blank=False)
    username = models.CharField(max_length=255, null=False, blank=False, unique=True)
    first_name = models.CharField(max_length=255, null=False, blank=False)
    last_name = models.CharField(max_length=255, null=False, blank=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class ResetPassword(models.Model):
    email = models.EmailField(null=False, blank=False)
    token = models.CharField(null=False, max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
