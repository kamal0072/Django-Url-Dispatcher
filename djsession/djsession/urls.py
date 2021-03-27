from django.contrib import admin
from django.urls import path
from school import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name='home'),
    path('setsession/',views.set_session,name='setsession'),
    path('getsession/',views.get_session,name='getsession'),
    path('delsession/',views.del_session,name='delsession'),
]
