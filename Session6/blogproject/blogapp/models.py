from django.db import models

# Create your models here.
class Article(models.Model):
        # 카테고리
        DRAMA = 'dr'
        MOVIE = 'mv'
        PROGRAMMING = 'pg'
        CATEGORY_CHOICES = (
            (DRAMA, "drama"),
            (MOVIE, 'movie'),
            (PROGRAMMING, 'programming')
        )
        title = models.CharField(max_length=200)
        content = models.TextField()
        category = models.CharField(
            max_length=3,
            choices=CATEGORY_CHOICES,
            default=DRAMA,
        )
        time = models.DateTimeField(null=True, default='')
        def __str__(self):
            return self.title