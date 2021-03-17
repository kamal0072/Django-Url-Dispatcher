from django.shortcuts import render

def main(request):
    title1='Django'
    return render(request,'school/main.html',{'title1':title1})

def about(request):
    title2="DRF"
    return render(request,'school/about.html',{'title2':title2})

def base(request):
    title3='Python'
    return render(request,'school/base.html',{'title3':title3})
