기본 예제에서는 다음을 테스트 한다.
* models
* views
* forms
* API

### Setup
`coverage`를 설치하고 `INSTALLED_APPS`에 추가 한다
```bash
pip install coverage
```

그리고 `coverage`를 실행 해보자
> 현재 원문의 `repo`에 있는 `django15` 앱은 실행이 `python3.6.5` 기준으로 실행 되지 않아서 본인의 `repo`에 있는 `app`을 사용 하면 된다.

```bash
coverage run manage.py test whatever -v 2
```
> 해당 명령을 실행하기 전에 `runserver`를 먼저 돌려 놓자. 그래야 셀레니움의 작동 된다.

그리고 보고서를 만들어 보자
```bash
coverage html
```
> 그러면 htmlcover에 html 파일들이 생긴것을 확인 할 수 있다.

