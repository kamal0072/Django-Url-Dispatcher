from django.db import models

# Create your models here.
class Student(models.Model):
    s_name=models.CharField(max_length=90)
    s_roll=models.IntegerField()
    s_email=models.EmailField(max_length=90)