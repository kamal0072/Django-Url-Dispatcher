from django.shortcuts import render
from django.contrib import messages
from .forms import SignUp

def sign(request):
    if request.method=='POST':
        fm=SignUp(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,"Now You Can Login!!!")

    else:
        fm=SignUp()
    return render(request,'school/signup.html',{'form':fm})
