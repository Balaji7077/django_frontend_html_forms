from django.db import models

# Create your models here.

class school(models.Model):
    Sname=models.CharField(max_length=100,primary_key=True)
    Slocation=models.CharField(max_length=100)
    Sprinciple=models.CharField(max_length=100)

    def __str__(self):
        return self.Sname