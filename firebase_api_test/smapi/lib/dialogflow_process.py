import dialogflow_v2 as dialogflow
from google.protobuf.json_format import MessageToDict
from django.conf import settings

_language_code = settings.DLF_LANGUAGE_CODE
_project_id = settings.DLF_PROJECT_ID


def _pave_dlf_dictionary(raw_dict):
    return {
        'fulfillment_text': raw_dict.get('fulfillmentText'),
        'fulfillment_messages': raw_dict.get('fulfillmentMessages'),
        'source': raw_dict.get('webhookSource'),
        'payload': raw_dict.get('webhookPayload'),
        'action': raw_dict.get('action'),
        'query_text': raw_dict.get('queryText')
    }


def detect_intent_texts(session_id, texts):
    dialogflow.SessionsClient()
    session_client = dialogflow.SessionsClient()

    session = session_client.session_path(_project_id, session_id)
    print('Session path: {}\n'.format(session))

    text_input = dialogflow.types.TextInput(
        text=texts,
        language_code=_language_code
    )
    query_input = dialogflow.types.QueryInput(
        text=text_input
    )

    response = session_client.detect_intent(
        session=session,
        query_input=query_input
    )

    return _pave_dlf_dictionary(MessageToDict(response.query_result))