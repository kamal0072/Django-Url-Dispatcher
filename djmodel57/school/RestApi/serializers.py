from school.models import Student
from rest_framework import serializers

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=['id','s_name','s_roll','s_email']
    