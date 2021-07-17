from django.db import models

# Create your models here.

class Post(models.Model):
    text1 = models.TextField()

    def __str__(self):
        return self.text1[:50]
