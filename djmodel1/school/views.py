from django.shortcuts import render
from .models import StudentModel

def studentView(request):
    stu=StudentModel.objects.all()
    # stu=StudentModel.objects.get(pk=1)
    
    return render(request,'school/home.html',{'stud':stu})