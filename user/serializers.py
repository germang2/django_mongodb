from rest_framework import serializers
from django.contrib.auth.models import User
from .models import CustomUser

class UserSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    email = serializers.EmailField()

class CustomUserSerializer(serializers.Serializer):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ]
    user = UserSerializer()
    age = serializers.IntegerField(min_value=0, max_value=120)
    gender = serializers.ChoiceField(GENDER_CHOICES)
    created_at = serializers.DateTimeField(read_only=True)

    """ validate that the user is unique, validating email """
    def validate_user(self, value):
        email = value['email']
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError('This email already exists')
        return value

 
    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['user']['email'],
            email=validated_data['user']['email'],
            first_name=validated_data['user']['first_name'],
            last_name=validated_data['user']['last_name']
        )
        return CustomUser.objects.create(
            user=user, 
            age=validated_data['age'],
            gender=validated_data['gender']
        )