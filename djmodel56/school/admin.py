from django.contrib import admin

# Register your models here.
from .models import School

@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display=['student_name','teacher_name','email','password']
    
