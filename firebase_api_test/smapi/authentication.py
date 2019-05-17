from drf_firebase_auth.authentication import FirebaseAuthentication
from firebase_admin import auth as firebase_auth
from drf_firebase_auth.settings import api_settings
from rest_framework import exceptions
from django.conf import settings


class FirebaseScopeAuthentication(FirebaseAuthentication):
    def decode_token(self, firebase_token):
        """
        Attempt to verify JWT from Authorization header with Firebase and
        return the decoded token
        """
        scope_name = settings.SCOPE_NAME
        try:
            claims = firebase_auth.verify_id_token(
                firebase_token,
                check_revoked=api_settings.FIREBASE_CHECK_JWT_REVOKED
            )
            if scope_name != '':
                if claims.get(scope_name) is None or claims.get(scope_name) is False:
                    raise exceptions.AuthenticationFailed(
                        '! Token claim permission denied !'
                    )
            return claims
        except ValueError as exc:
            raise exceptions.AuthenticationFailed(
                'JWT was found to be invalid, or the App’s project ID cannot '
                'be determined.'
            )
        except firebase_auth.AuthError as exc:
            if exc.code == 'ID_TOKEN_REVOKED':
                raise exceptions.AuthenticationFailed(
                    'Token revoked, inform the user to reauthenticate or '
                    'signOut().'
                )
            else:
                raise exceptions.AuthenticationFailed(
                    'Token is invalid.'
                )
