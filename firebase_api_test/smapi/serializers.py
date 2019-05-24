from rest_framework import serializers
from smapi import models


class HelloWorldSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'description',
        )
        model = models.HelloWorld


class NoModelTestSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    comments = serializers.CharField(max_length=255)
