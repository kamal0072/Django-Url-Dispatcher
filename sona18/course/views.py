from django.shortcuts import render

def course(request):
    return render(request,'course/courseinfo.html')