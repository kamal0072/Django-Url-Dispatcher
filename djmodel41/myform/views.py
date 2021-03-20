from django.shortcuts import render
from .forms import EmployeForm

def emplyeview(request):
    if request.method=="POST":
        em=EmployeForm(request.POST)
        if em.is_valid():
            print("Cleaned Name:-",em.cleaned_data['ename'])
            print("Cleaned Password:-",em.cleaned_data['epass'])
            print("Cleaned Email:-",em.cleaned_data['email'])
    else:
        print("Data Coming From Get Request-------")
        em=EmployeForm()
    return render(request,'myform/home.html',{'emp':em})

