from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']  # masih bisa minta username tapi tidak wajib sebagai login

    def __str__(self):
        return self.email
