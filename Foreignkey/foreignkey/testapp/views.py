from django.shortcuts import render
from .serializers import SingerSerializer,SongSerializer
from rest_framework import viewsets
from .models import *

# Create your views here.
class SingerModelViewSet(viewsets.ModelViewSet):
    queryset=Singer.objects.all()
    serializer_class=SingerSerializer
class SongModelViewSet(viewsets.ModelViewSet):
    #name = 'singer'
    queryset=Song.objects.all()
    serializer_class=SongSerializer
    
