from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Notes
from .serializers import NotesSerializer

# Create your views here.
class NotesViewSet(viewsets.ModelViewSet):
    serializer_class = NotesSerializer
    queryset = Notes.objects.all()

@api_view(['GET'])
def notes_user(request, id):
    """
    View to get all notes of a user
    """
    notes = Notes.objects.filter(custom_user=id)
    serializer = NotesSerializer(notes, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)