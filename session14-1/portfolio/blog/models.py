from django.db import models
from django.contrib.auth.models import User
from django.contrib import auth
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 200)
    content = models.TextField()
    date_created = models.DateField(auto_now_add=True, null=True)
    image = models.ImageField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    def __str__(self):
        return f'{self.title} | {self.author}'

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    comment = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return(self)