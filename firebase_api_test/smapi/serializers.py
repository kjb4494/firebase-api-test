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


class DialogflowResponse(serializers.Serializer):
    fulfillment_text = serializers.CharField(allow_null=False)
    fulfillment_messages = serializers.ListField(allow_null=True)
    source = serializers.CharField(allow_null=True)
    payload = serializers.DictField(allow_null=True)
    action = serializers.CharField(allow_null=True)
    query_text = serializers.CharField(allow_null=True)
