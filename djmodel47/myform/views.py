from django.shortcuts import render
from .forms import EmployeForm
from .models import Student

def emplyeview(request):
    if request.method=="POST":
        em=EmployeForm(request.POST)
        if em.is_valid():
            ename=em.cleaned_data['ename']
            epass=em.cleaned_data['epass']
            email=em.cleaned_data['email']
            stu=Student(ename=ename,epass=epass,email=email)
            print(stu)
            # stu=Student(id=1,ename=ename,epass=epass,email=email)
            # stu=Student(id=1)
            stu.save()
            em=EmployeForm()
            # stu.delete()
    else:
        print("Data Coming From Get Request-------")
        em=EmployeForm()
    return render(request,'myform/home.html',{'emp':em})

