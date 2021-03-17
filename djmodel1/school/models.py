from django.db import models

class StudentModel(models.Model):
    s_roll=models.IntegerField()
    s_name=models.CharField(max_length=90)
    s_address=models.CharField(max_length=90)
    s_email=models.EmailField(max_length=90)
    s_pass=models.CharField(max_length=90)

