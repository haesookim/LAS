from django.db import models

class Page(models.Model):
    title = models.CharField(max_length = 255)
    text = models.TextField()

    def __str__(self):
        return self.title
# Create your models here.
