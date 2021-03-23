from django.urls import path,include
from rest_framework.routers import DefaultRouter
from school.RestApi import views

router=DefaultRouter()
router.register('student',views.StudentModelVIew,basename='student')

urlpatterns = [
    path('',include(router.urls)),
    path('auth-stu/',include('rest_framework.urls')),
]
