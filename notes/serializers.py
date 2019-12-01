from rest_framework import serializers
from .models import Notes
from user.serializers import CustomUserSerializer

class NotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = ['id', 'title', 'body', 'created_at', 'custom_user']