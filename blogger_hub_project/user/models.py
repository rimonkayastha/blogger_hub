from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models
from .managers import CustomUserManager

# Create your models here.
class CustomUser(AbstractUser):
    email = models.EmailField('Email address', unique=True)
    username = models.CharField('Username', max_length=150, unique=True, blank=False)
    profile_image = models.ImageField(blank = True, null = True, upload_to='images/')

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email