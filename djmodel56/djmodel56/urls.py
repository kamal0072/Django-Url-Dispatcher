
from django.contrib import admin
from django.urls import path
from school import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/',views.student_form,name='student'),
    path('studentsucess/',views.student_success,name='studentsuccess'),
    path('teacher/',views.teacher_form,name='teacher'),
    path('teachersuccess/',views.teacher_success,name='teachersuccess'),
]
