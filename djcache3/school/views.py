from django.shortcuts import render
# 
#Data base caching 
# @cache_page(10)
def home(request):
    return render(request,'school/home.html')

def about(request):
    return render(request,'school/about.html')