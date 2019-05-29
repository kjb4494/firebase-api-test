from rest_framework import serializers


class DialogflowResponse(serializers.Serializer):
    fulfillment_text = serializers.CharField(allow_null=False)
    fulfillment_messages = serializers.ListField(allow_null=True)
    source = serializers.CharField(allow_null=True)
    payload = serializers.DictField(allow_null=True)
    action = serializers.CharField(allow_null=True)
    query_text = serializers.CharField(allow_null=True)
