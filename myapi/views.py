from django.shortcuts import render
from .models import Hero
from .serializers import HeroSerializers
from rest_framework import viewsets

class HeroViewSet(viewsets.ModelViewSet):
    queryset=Hero.objects.all()
    serializer_class=HeroSerializers
