
from django.contrib import admin
from django.urls import path
from school import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.main,name='main'),
    path('about/',views.about,name='about'),
    path('base/',views.base,name='base'),
]
