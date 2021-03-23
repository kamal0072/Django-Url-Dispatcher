
from django.contrib import admin
from django.urls import path,include
from school import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/',views.studentview,name='home'),
    path('api/',include('school.RestApi.urls')),
]
