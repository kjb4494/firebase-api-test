# Firebase REST API Test

#### 메모장
- manage.py와 동일한 경로에 firebase-sac.json 파일이 요구됨
- 아래와 같은 요청으로 API를 사용할 수 있음
  ```
  curl --request GET \
    --url http://localhost:8010/api/v1/ \
    --header 'authorization: JWT <token>'
  ```
- settings에서 SCOPE_NAME을 설정해서 사용자 접근제어를 사용할 수 있음
  - 빈 문자열일 경우 사용자 접근제어를 사용하지 않음
  
- settings 추가된 항목
  - INSTALLED_APPS
    ```
    INSTALLED_APPS = [
    ...
    'smapi',
    'rest_framework',
    'drf_firebase_auth'
    ]
    ```
  - REST_FRAMEWORK
    ```
    REST_FRAMEWORK = {
        'DEFAULT_AUTHENTICATION_CLASSES': [
            'rest_framework.authentication.SessionAuthentication',
            'smapi.authentication.FirebaseScopeAuthentication',
        ]
    }
    ```
  - DRF_FIREBASE_AUTH
    ```
    DRF_FIREBASE_AUTH = {
        'FIREBASE_SERVICE_ACCOUNT_KEY': 'firebase-sac.json',
        'FIREBASE_CREATE_LOCAL_USER': True,
        'FIREBASE_ATTEMPT_CREATE_WITH_DISPLAY_NAME': True,
        'FIREBASE_AUTH_HEADER_PREFIX': 'JWT',
        'FIREBASE_CHECK_JWT_REVOKED': True,
        'FIREBASE_AUTH_EMAIL_VERIFICATION': False
    }
    ```
  - SCOPE_NAME
    ```
    SCOPE_NAME = ''
    ```