
from django.contrib import admin
from django.urls import path
from school import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.about,name='home'),
    path('student/<my_id>/',views.show,name='detail'),
]
