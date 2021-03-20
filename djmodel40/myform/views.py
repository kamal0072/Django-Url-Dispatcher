from django.shortcuts import render
from .forms import EmployeForm

def emplyeview(request):
    if request.method=="POST":
        em=EmployeForm(request.POST)
        if em.is_valid():
            print("Name:",em.cleaned_data['ename'])
            print("Password:",em.cleaned_data['epass'])
            print("Email:",em.cleaned_data['eemail'])
            print("Father Name:",em.cleaned_data['fname'])
            print("agree",em.cleaned_data['agree'])
    else:
        print("Data Coming From Get Request-------")
        em=EmployeForm()
    return render(request,'myform/home.html',{'emp':em})

