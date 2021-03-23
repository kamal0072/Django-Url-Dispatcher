from django.contrib import admin

# Register your models here.
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=['id','s_name','s_roll','s_email']
    
