from django.shortcuts import render
from rest_framework import generics
from smapi import models
from . import serializers


# Create your views here.
class ListHelloWolrd(generics.ListCreateAPIView):
    queryset = models.HelloWorld.objects.all()
    serializer_class = serializers.HelloWorldSerializer


class DetailHelloWolrd(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.HelloWorld.objects.all()
    serializer_class = serializers.HelloWorldSerializer
