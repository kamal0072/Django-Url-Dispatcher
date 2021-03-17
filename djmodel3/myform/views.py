from django.shortcuts import render

from .forms import EmployeForm

def emplyeview(request):
    # em=EmployeForm(auto_id='some_%s')
    # em=EmployeForm(auto_id=True)
    # em=EmployeForm(auto_id=False)
    # em=EmployeForm(auto_id='anystring')
    em=EmployeForm(auto_id=True,label_suffix=':')
    return render(request,'myform/home.html',{'emp':em})