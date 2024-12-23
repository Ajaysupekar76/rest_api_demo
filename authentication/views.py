from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import RegisterSerializer

class RegisterUserAPIView(generics.CreateAPIView):
    serializer_class = RegisterSerializer



# views.py
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainPairSerializer

class LoginAPIView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
