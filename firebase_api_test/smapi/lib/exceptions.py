from rest_framework.exceptions import APIException


class ParamsBadRequestError(APIException):
    status_code = 400
    default_detail = 'Missing required parameters.'
    default_code = 'Bad Request'
