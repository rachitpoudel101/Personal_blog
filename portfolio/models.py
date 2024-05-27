from django.db import models


class Projects(models.Model):
    title = models.CharField(max_length=50)
    discription = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)


def __str__(self):
    return self.title
