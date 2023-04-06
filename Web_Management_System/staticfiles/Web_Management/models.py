from django.db import models

class Books(models.Model):
    book = models.TextField(max_length=255)
    finished = models.BooleanField(default=False)
    review = models.TextField(max_length=500)

class Movies(models.Model):
    movie = models.TextField(max_length=255)
    finished = models.BooleanField(default=False)
    review = models.TextField(max_length=500)