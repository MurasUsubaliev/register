from django.contrib.auth.models import AbstractUser
from django.db import models

class Region(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class User(AbstractUser):
    email = models.EmailField(unique=True)  # Сделайте поле email уникальным
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.username

