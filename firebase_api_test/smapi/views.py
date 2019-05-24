from django.shortcuts import render
from rest_framework import generics, views
from rest_framework.response import Response
from smapi import models
from . import serializers


# Create your views here.
class ListHelloWolrd(generics.ListCreateAPIView):
    queryset = models.HelloWorld.objects.all()
    serializer_class = serializers.HelloWorldSerializer


class DetailHelloWolrd(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.HelloWorld.objects.all()
    serializer_class = serializers.HelloWorldSerializer


class NoModelTest(views.APIView):
    def get(self, request):
        no_model_data = {
            "title": "first comments",
            "comments": "hello! this is no model api!"
        }
        results = serializers.NoModelTestSerializer(no_model_data, many=False).data
        return Response(results)
