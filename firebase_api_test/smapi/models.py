from django.db import models


# Create your models here.
class HelloWorld(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.title


_dialogflow_fields = (
    'fulfillment_text',
    'fulfillment_messages',
    'source',
    'payload',
    'action',
    'query_text'
)

_bad_request_fields = (
    'detail',
)


# Create your models here.
class Dialogflow:
    def __init__(self, **kwargs):
        for field in _dialogflow_fields:
            setattr(self, field, kwargs.get(field, None))
