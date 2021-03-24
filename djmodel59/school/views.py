from django.shortcuts import render

from django.contrib.auth.forms import UserCreationForm

def sign(request):
    if request.method=='POST':
        fm=UserCreationForm(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm=UserCreationForm()
    return render(request,'school/signup.html',{'form':fm})
