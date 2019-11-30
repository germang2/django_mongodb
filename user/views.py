from django.shortcuts import render
from rest_framework import viewsets
from .models import CustomUser
from .serializers import CustomUserSerializer
from django.contrib.auth.models import User

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()