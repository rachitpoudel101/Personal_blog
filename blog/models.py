from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    discription = models.TextField()
    date = models.DateField()