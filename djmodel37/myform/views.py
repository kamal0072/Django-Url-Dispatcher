from django.shortcuts import render

from .forms import EmployeForm

def emplyeview(request):
    em=EmployeForm()
    return render(request,'myform/home.html',{'emp':em})