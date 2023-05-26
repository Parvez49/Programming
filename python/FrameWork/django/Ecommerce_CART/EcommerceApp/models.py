from django.db import models

# Create your models here.


class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    ques=models.TextField(max_length=500)
    ph=models.IntegerField()

    def __init__(self):
        return self.id
