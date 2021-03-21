from django.db import models

class School(models.Model):
    student_name=models.CharField(max_length=90)
    teacher_name=models.CharField(max_length=90)
    email=models.EmailField(max_length=90)
    password=models.CharField(max_length=90)