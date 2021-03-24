from django.contrib import admin
from django.urls import path
from school import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.sign,name='signp'),
    path('login/',views.userlogin,name='login'),
    path('profile/',views.profile_page,name='profile'),
    path('logout/',views.logoutpage,name='logout')
]
