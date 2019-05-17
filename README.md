# Firebase REST API Test

#### 메모장
- manage.py와 동일한 경로에 firebase-sac.json 파일이 요구됨
- 아래와 같은 요청으로 API를 사용할 수 있음
    ```
    curl --request GET \
      --url http://localhost:8010/api/v1/ \
      --header 'authorization: JWT <token>'
    ```
