from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from .models import User
from django.views.generic.base import TemplateView,RedirectView,View

class UserAddShowView(TemplateView):
      template_name='enroll/addandshow.html'

      def get_context_data(self, **kwargs):
          context = super().get_context_data(**kwargs)
          fm = StudentRegistration()  
          stud = User.objects.all()
          context={'stu':stud,'form':fm}
          return context

      def post(self,request):
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
          nm = fm.cleaned_data['name']
          em = fm.cleaned_data['email']
          pw = fm.cleaned_data['password']
          reg = User(name=nm, email=em, password=pw)
          reg.save()
        return HttpResponseRedirect('/')


class UserDeleteView(RedirectView):
      url='/'
      def get_redirect_url(self,*args, **kwargs):
        del_id=kwargs['id']
        User.objects.get(pk=del_id).delete()
        return super().get_redirect_url(*args, **kwargs)


class UserUpdateView(View):
    def get(self,request,id):
      pi = User.objects.get(pk=id)
      fm = StudentRegistration(instance=pi)
      return render(request, 'enroll/updatestudent.html', {'form':fm})
        
    def post(self,request,id):
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
          fm.save()
        # return render(request, 'enroll/updatestudent.html', {'form':fm})
        return HttpResponseRedirect('/')
      
        