from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'school/schoolone.html')

def about(request):
    name={'course':'pyhton'}
    return render(request,'school/about.html',{'nm':name})