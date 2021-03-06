#from django.shortcuts import render
from .models import StudentModelViewSet
from .serializers import StudentSerializer
from rest_framework import viewsets

# Create your views here.
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = StudentModelViewSet.objects.all()
    serializer_class = StudentSerializer
