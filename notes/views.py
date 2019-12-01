from django.shortcuts import render
from rest_framework import viewsets
from .serializers import NotesSerializer
from .models import Notes
# Create your views here.
class NotesViewSet(viewsets.ModelViewSet):
    serializer_class = NotesSerializer
    queryset = Notes.objects.all()
