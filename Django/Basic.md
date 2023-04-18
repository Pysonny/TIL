# Django 사용법
1. 실전 ( 로컬버전 )
   1. 생성
   ``` python -m venv [가상환경이름] ```
   2. 활성화 
      1. (Terminal)
      ``` source [가상환경이름]/bin/activate ```
      ` . venv/bin/activate` 도 가능
   
      2. python interpreter 설정 (vscode)
         1. cmd + shift + P 입력
         2. `python:Select Interpreter` 검색 후 클릭
         3. 내가 만든 서버 클릭
         4. 터미널 생성
      3. 비활성화
      ``` deactivate ```
   3. 현재 가상환경인지 확인
   ``` pip list ```
   4. django 설치
   ``` pip install django==3.2.18 ```
   5. 의존성 파일 생성 ( 패키지 설치시마다 진행)
   ``` pip freeze > requirements.txt ```
   6. .gitignore 추가
      1. https://www.toptal.com/developers/gitignore
      2. 생성 후 추가하기
   7.  django 프로젝트 생성
   ``` django-admin startproject [프로젝트명] . ```( `.` 현재위치)
   8.  django 서버 실행
   ``` python manage.py runserver ``` 
   9. 앱 생성
   ``` python manage.py startapp articles ```
   10. 앱 등록 (settings.py > 'INSTALLED_APPS')
   ``` articles, ```
   > 앱을 생성한 후에 등록해야 함! / 등록 후 생성은 불가능
   11. URLs (firstpjt > urls.py)
      1. `from articles import views` 추가
      2. `urlpatterns`에 `path('articles/', views.index),` 추가 / articles/ 는 url 주소 이름(수정가능!)
   12. View (articles > views.py)
      1. `def index(request):
            return render(request,'articles/index.html')`
   13. Template (articles)
      1.  `articles` 앱 폴더 안에 `templates` 폴더 작성
      2.  `templates` 폴더 안에 템플릿 페이지 작성
      > 반드시 `templates` 폴더명이여야 하며 개발자가 직접 생성해야함! 

## MODEL 

1. 작성
> articles > models.py
``` py
class Article(models.Model):
    # 필드이름 = 데이터 타입(제약조건)
    title = models.CharField(max_length=10) # 길이제한 O
    content = models.TextField() # 길이제한 X
``` 

2. migration 생성
> 터미널
``` python manage.py makemigrations ```   

3. 전달
> 터미널 
``` python manage.py migrate ```


## 초기설정
- APP에 urls.py 추가하기
``` py
from django.urls import path
from . import views

app_name = 'todos'
urlpatterns = [
   path('', views.index, name='index') ,
]
```
- 기존 Projects에 urls.py 에 연결하기

```py
from django.urls import path, include

urlpatterns = [
   path('todos/', include('todos.urls')),
]
```

- views.py
```py
from .models import Todo

def index(request):
    todos = Todo.objects.all()
    context = {
        'todos' : todos , 
    }
    return render(request, 'todos/index.html', context)

```
- templates/todos 에 index.html 생성


## base 템플릿 생성

templates/base.html 생성

settings.py => TEMPLATES
'DIRS" : [기본 템플릿 경로 외에 추가 경로를 작성],
ex[ BASE_DIR / 'my_templates']


```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-KK94CHFLLe+nY2dmCWGMq91rCGa5gtU4mk92HdvYe+M/SXH301p5ILy+dN9+nJOZ" crossorigin="anonymous">
    <link rel="stylesheet" href="{% static 'style.css' %}">
</head>
<body>
    {% block content %}
    {% endblock content %}
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js" integrity="sha384-w76AqPfDkMBDXo30jS1Sgez6pr3x5MlQ1ZAGC+nuZB+EYdgRZgiwxhTBTkF7CXvN" crossorigin="anonymous"></script>

</body>
</html>
```
base사용할 템플릿에

```html
{% extends 'base.html' %}
{% load static %}

{% block content %}

{% endblock content %}
```

