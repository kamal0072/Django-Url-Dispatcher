
from django.shortcuts import render


def show(request,my_id):
    return render(request,'school/home.html',{'id':my_id})

def about(request):
    return render(request,'school/about.html')