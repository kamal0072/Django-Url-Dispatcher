from django.shortcuts import render


def set_session(request):
    request.session['name']='sonam'
    request.session['lkamal']='kamalkhan'
    return render(request,'myapp/setsession.html')


def get_session(request):
    name=request.session['name']
    lname=request.session['lkamal']
    return render(request,'myapp/getsession.html',{'nm':name,'lnm':lname})

def del_session(request):
    if 'name' in request.session:
        del request.session['name']
    return render(request,'myapp/delsession.html')
