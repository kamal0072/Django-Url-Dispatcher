from django.shortcuts import render,HttpResponseRedirect
from django.contrib import messages
from .forms import SignUp
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
 
 
 #signup Form FBV
def sign(request):
    if request.method=='POST':
        fm=SignUp(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,"Now You Can Login!!!")

    else:
        fm=SignUp()
    return render(request,'school/signup.html',{'form':fm})

#userLogin Form
def userlogin(request):
    if request.method=='POST':
        log_in=AuthenticationForm(request=request,data=request.POST)
        if log_in.is_valid():
            uname=log_in.cleaned_data['username']
            upass=log_in.cleaned_data['password']
            user=authenticate(username=uname,password=upass)
            if user is not None:
                login(request,user)
                messages.success(request,'Login Successfully!!!!!')
                return HttpResponseRedirect('/profile/')
                # return render(request,'school/profile.html')
    else:
        log_in=AuthenticationForm()
    return render(request,'school/loginform.html',{'login':log_in})


def profile_page(request):
    return render(request,'school/profile.html')


#Log Out Function
def logoutpage(request):
    logout(request)
    return HttpResponseRedirect('/login/')