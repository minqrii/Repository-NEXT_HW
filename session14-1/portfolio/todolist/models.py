from django.db import models
from django.contrib.auth.models import User
from django.contrib import auth
# Create your models here.
class Todolist(models.Model):
    todo = models. CharField(max_length = 200, verbose_name="할일제목")
    todocontent = models.TextField(verbose_name="할일내용")
    date_created = models.DateField(auto_now_add=True, null=True)
    date_deadline = models.DateField(verbose_name="마감기한")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todos")
    def __str__(self):
        return f'{self.todo} | {self.todocontent} | {self.date_deadline}'
