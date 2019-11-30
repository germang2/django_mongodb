from rest_framework import serializers
from django.contrib.auth.models import User
from .models import CustomUser
from rest_framework.validators import UniqueValidator

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
    id = serializers.IntegerField(read_only=True)
    user = UserSerializer()
    age = serializers.IntegerField(min_value=0, max_value=120)
    gender = serializers.ChoiceField(GENDER_CHOICES)
    created_at = serializers.DateTimeField(read_only=True)

    """ validate that the user is unique, validating email """
    def create(self, validated_data):
        email = value['email']
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

    def update(self, instance, validated_data):
        """ Validate that email doesn't exists in another user """
        email = validated_data['user']['email']
        user_instance = instance.user
        user = validated_data['user']
        user_instance.first_name = user['first_name']
        user_instance.last_name = user['last_name']
        user_instance.email = user['email']
        user_instance.username = user['email']
        user_instance.save()
        instance.age = validated_data['age']
        instance.gender = validated_data['gender']
        instance.save()
        return instance