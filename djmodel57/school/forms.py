from .models import Student
from django import forms

class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields=['id','s_name','s_roll','s_email']
        labels={'s_name':'STUDENT NAME','s_roll':'STUDENT ROLL NUMBER',
        's_email':'STUDENT EMAIL'}