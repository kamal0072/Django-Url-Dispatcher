from django.contrib import admin
from django.urls import path
from school import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.sign,name='signp'),
    path('login/',views.userlogin,name='login'),
    path('profile/',views.profile_page,name='profile'),
    path('logout/',views.logoutpage,name='logout'),
    path('passwaedchange/',views.change_pass,name='passwaedchange'),
    path('setpass/',views.setuserpassword,name='setpass'),
    # path('set/',views.setcookie,name='setcookie'),
    path('setsigned/',views.setsignedcookie,name='setsigned'),
    # path('get/',views.getcookie,name='getcookie'),
    path('getsignedcookie/',views.getsignedcookie,name='getsignedcookie'),
    # path('del/',views.delcookie,name='delcookie'),
    path('del/',views.delcookie,name='delcookie'),
]
