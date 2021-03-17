from django.contrib import admin
from .models import StudentModel

@admin.register(StudentModel)
class StudentModelAdmin(admin.ModelAdmin):
    list_display=['id','s_roll','s_name','s_address','s_email','s_pass']
    
