from django.db import models

# Create your models here.
class Student(models.Model):
    Sname=models.CharField(max_length=100,primary_key=True)
    Sid=models.IntegerField()
    Semail=models.EmailField()
    