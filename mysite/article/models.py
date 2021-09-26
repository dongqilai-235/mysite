from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=30)
    context = models.TextField()


objects = models.Manager()