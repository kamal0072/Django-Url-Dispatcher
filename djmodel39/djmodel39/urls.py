from django.contrib import admin
from django.urls import path
from myform import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.emplyeview,name='home'),
]
