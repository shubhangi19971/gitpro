from django.shortcuts import render
from  rest_framework import viewsets
from .serializers import Employee, EmployeeSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
