from django.shortcuts import render
from django.contrib import messages
from .forms import UserCreationForm

def userloginform(request):
    if request.method=='POST':
        fm=UserCreationForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,'Now You Can Login!!!')
    else:
        fm=UserCreationForm()
    return render(request,'school/loginform.html',{'form':fm})