from django import forms
from .models import School

class StudentDetail(forms.ModelForm):
    class Meta:
        model=School
        fields=['student_name','email','password']
        labels={'student_name':'STUDENT NAME','email':'EMAIL ADDRESS','password':'PASSWORD'}
        widgets={'student_name':forms.TextInput(attrs={'placeholder':'abhi@gmail.com'}),
        'email':forms.TextInput(attrs={'placeholder':'abhi@gmail.com'}),
        'password':forms.PasswordInput()}
        help_text={'student_name':'Enter your Name Here OK'}
        error_message={'student_name':'Name is mandatory'}

class TeacherDetail(StudentDetail):
    class Meta(StudentDetail.Meta):
        fields=['teacher_name','email','password']
        labels={'teacher_name':'TEACHER NAME','email':'EMAIL ADDRESS',
        'password':'PASSWORD'}
        widgets={'teacher_name':forms.TextInput(attrs={'placeholder':'james'}),
        'email':forms.TextInput(attrs={'placeholder':'abc@gmail.com'}),
        'password':forms.TextInput(attrs={'placeholder':'J@mes123'}),
        'password':forms.PasswordInput}
