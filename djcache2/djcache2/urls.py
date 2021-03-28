
from django.contrib import admin
from django.urls import path
from school import views
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',cache_page(20)(views.home),name='home'),
    path('about/',cache_page(50)(views.about),name='about'),
]
