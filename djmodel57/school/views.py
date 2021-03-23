from django.shortcuts import render

# Create your views here.
from .models import Student 
from .forms import StudentForm
from django.contrib import messages


def studentview(request):
    if request.method=='POST':
        stu1=StudentForm(request.POST)
        if stu1.is_valid():
            sname=stu1.cleaned_data['s_name']
            sroll=stu1.cleaned_data['s_roll']
            semail=stu1.cleaned_data['s_email']
            stu=Student(s_name=sname,s_roll=sroll,s_email=semail)
            stu.save()
            messages.success(request,'Your Data has been Saved')
            messages.info(request,'info message')
            messages.debug(request,'debug message')
            print(messages.get_level(request))

            messages.set_level(request,messages.DEBUG)
            
            print(messages.get_level(request))
            stu1=StudentForm()
    else:
        stu1=StudentForm()
    return render(request,'school/regis.html',{'student':stu1})
