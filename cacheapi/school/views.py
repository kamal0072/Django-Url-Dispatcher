from django.shortcuts import render
from django.core.cache import cache 
#Data base caching 
# @cache_page(10)
def home(request):
    # mv=cache.get('movie','has_expired')
    # if mv=='has_expired':
    #     cache.set('movie','The One and ',20)
    #     mv=cache.get('movie')
    # return render(request,'school/home.html',{'fm':mv})
    mv=cache.get_or_set('fees',45000,20)
    return render(request,'school/home.html',{'fm':mv})

def home(request):
    data={'name':'kamal','roll':230}
    cache.set_many(data,20)
    sv=cache.get_many(data)
    return render(request,'school/home.html',{'fm':sv})

def about(request):
    return render(request,'school/about.html')