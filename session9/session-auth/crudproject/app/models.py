from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200, default=None)
    content = models.TextField(default=None)
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE, default=None, related_name='posts')
    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', default=None)
    content = models.TextField(default=None)
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE, default=None, related_name='comments')