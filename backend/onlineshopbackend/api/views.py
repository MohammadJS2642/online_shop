from django.shortcuts import render
from django.contrib.auth.models import User
from api.serializers import UserSerializer
from rest_framework import generics
from rest_framework.response import Response

# Create your views here.


class UserList(generics.ListCreateAPIView):
    '''
    get all users and create new user
    '''
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateAPIView):
    '''
    for retrieve and update users
    '''
    queryset = User.objects.all()
    serializer_class = UserSerializer
