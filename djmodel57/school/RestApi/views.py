from school.RestApi.serializers import StudentSerializer
from school.models import Student 
from rest_framework import viewsets


class StudentModelVIew(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer