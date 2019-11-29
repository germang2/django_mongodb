from rest_framework import serializers
from .models import CustomUser as User

class UserSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    email = serializers.EmailField()

class CustomUserSerializer(serializers.Serializer):
    user = UserSerializer()
    age = serializers.IntegerField()
    gender = serializers.CharField(max_length=20)
    created_at = serializers.DateTimeField(read_only=True)