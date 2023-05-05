from django.db import models

# Create your models here.

class Lesson(models.Model):
    ls_name=models.CharField(max_length=50)
    name=models.CharField(max_length=50)

