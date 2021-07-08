from django.db import models
from django.contrib.auth.models import User
from django.contrib import auth
# Create your models here.
class TodoList(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=200, verbose_name="할일제목", null=True)
    date_created = models.DateField(auto_now_add=True, verbose_name="생성날짜", null=True)
    date_deadline = models.DateField(verbose_name="데드라인", null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts', null=True)
    def __str__(self):
        return f'{self.title} | {self.content} | {self.date_created} | {self.date_deadline}'

class Comment(models.Model):
    todo = models.ForeignKey(TodoList, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField(verbose_name="댓글")

class TodoList_images(models.Model):
    todo = models.ForeignKey(TodoList, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='todo/image/%Y/%m', blank=True)


class TodoList_files(models.Model):
    todo = models.ForeignKey(TodoList, on_delete=models.CASCADE)
    files = models.FileField(upload_to='todo/files/%Y/%m', blank=True)
