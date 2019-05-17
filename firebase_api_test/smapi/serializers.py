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
