from rest_framework import views
from rest_framework.response import Response
from smapi.lib.dialogflow_process import detect_intent_texts
from smapi.lib.decorators import requires_params
from . import serializers
import hashlib


# Create your views here.
class SmbotTextQuery(views.APIView):
    @requires_params(['query_text', 'test'])
    def get(self, request):
        session_id = hashlib.md5(request.META.get('HTTP_AUTHORIZATION').encode('utf-8')).hexdigest()
        res = detect_intent_texts(session_id, request.GET.get('query_text'))
        results = serializers.DialogflowResponse(res, many=False).data
        return Response(results)
