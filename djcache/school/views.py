from django.shortcuts import render

#Data base caching 
def home(request):
    return render(request,'school/home.html')