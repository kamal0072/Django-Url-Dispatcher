
from django.contrib import admin
from django.urls import path,include
from core import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('cor/',include('course.urls'),name='cor'),
]
