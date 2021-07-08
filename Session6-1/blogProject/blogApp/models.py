from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    class meta:
        verbose_name_plural = 'categories'
    
    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.CASCADE)
    publish = models.DateTimeField(auto_now=True)
    content = models.TextField()

    def __str__(self):
        return self.title 