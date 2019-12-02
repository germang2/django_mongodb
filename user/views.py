from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import CustomUser
from .serializers import CustomUserSerializer
from django.contrib.auth.models import User
import json

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()

    def list(self, request, *args, **kwargs):
        params = request.query_params
        filters = params['query'] if 'query' in params else None
        queryset = CustomUser.objects.all()
        if filters is not None:
            try:
                json_query = json.loads(filters)
                if 'name' in json_query:
                    queryset = queryset.filter(user__first_name__icontains=json_query['name'])
                if 'last_name' in json_query:
                    queryset = queryset.filter(user__last_name__icontains=json_query['last_name'])
                if 'gender' in json_query:
                    queryset = queryset.filter(gender=json_query['gender'].lower())
                if 'email' in json_query:
                    queryset = queryset.filter(user__email__icontains=json_query['email'])
            except:
                pass

        page = self.paginate_queryset(queryset)
        serializer = CustomUserSerializer(queryset, many=True)
        return self.get_paginated_response(serializer.data)