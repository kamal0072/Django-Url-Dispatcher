from django.db import models

class Student(models.Model):
    ename=models.CharField(max_length=90)
    epass=models.CharField(max_length=90)
    email=models.EmailField(max_length=90)