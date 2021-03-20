from django.shortcuts import render
from .forms import EmployeForm

def emplyeview(request):
    if request.method=="POST":
        em=EmployeForm(request.POST)
        if em.is_valid():
            print("Validated Data From Post")
            print("Name:",em.cleaned_data['ename'])
            print("Name:",em.cleaned_data['epass'])
            print("Email",em.cleaned_data['eemail'])
            em=EmployeForm()
    else:
        print("Data Coming From Get Request-------")
        em=EmployeForm()
    return render(request,'myform/home.html',{'emp':em})