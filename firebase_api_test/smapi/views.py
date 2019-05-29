from rest_framework import generics, views
from rest_framework.response import Response
from smapi import models
from . import serializers
from smapi.lib.dialogflow_process import detect_intent_texts
import hashlib


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


class SmbotTextQuery(views.APIView):
    def get(self, request):
        query_text = request.GET.get('query_text')
        session_id = hashlib.md5(request.META.get('HTTP_AUTHORIZATION').encode('utf-8')).hexdigest()
        res = detect_intent_texts(session_id, query_text)
        results = serializers.DialogflowResponse(res, many=False).data
        return Response(results)
