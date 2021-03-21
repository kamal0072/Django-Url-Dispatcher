from django.shortcuts import render
from .models import School
from .forms import StudentDetail,TeacherDetail

def student_form(request):
    if request.method=="POST":
        stu=StudentDetail(request.POST)
        if stu.is_valid():
            stu.save()
    else:
        stu=StudentDetail()
    return render(request,'school/student.html',{'stu1':stu})

def student_success(request):
    return render(request,'school/studentsuccess.html')



def teacher_form(request):
    if request.method=='POST':
        tea=TeacherDetail(request.POST)
        if tea.is_valid():
            tea.save()
    else:
        tea=TeacherDetail()
    return render(request,'school/teacher.html',{'tea1':tea})
    
def teacher_success(request):
    return render(request,'school/teachersuccess.html')