from django.shortcuts import render,HttpResponse


def home(request):
    ct=request.session.get('count',0)
    newcount=ct+1
    request.session['count']=newcount
    return render(request,'school/home.html',{'ct':newcount})

# Create your views here.
def set_session(request):
    request.session['name']='peter'
    request.session['key']=4
    return render(request,'school/setsession.html')

def get_session(request):
    if 'name' in request.session:
        name=request.session['name']
        key=request.session['key']
        request.session.modified=True
        return render(request,'school/getsession.html',{'nm':name,'key':key})
    else:
        return HttpResponse('Session Expired')

def del_session(request):
    request.session.flush()
    request.session.clear_expired()
    return render(request,'school/delsession.html')