from django.db import models
from django.contrib.auth.models import User
from django.contrib import auth
# Create your models here.
class Album(models.Model):
    image = models.ImageField(blank=True)
    detail = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='albums')