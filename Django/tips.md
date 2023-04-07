
# Django 사용법

1. vscode extension 설치

   1. extension 
      1. Django
      2. SQLite Viewer

   2. json 설정
      1.  ctrl(command) + shift + p → json검색 → Preferences: Open User Settings (JSON) 선택
      2. 설정 코드 붙혀넣기 
        ```jsx
            // settings.json
            {
            // Django
            "files.associations": {
                "**/*.html": "html",
                    "**/templates/**/*.html": "django-html",
                "**/templates/**/*": "django-txt",
                "**/requirements{/**,*}.{txt,in}": "pip-requirements"
            },
            "emmet.includeLanguages": {
                "django-html": "html"
            }
            }
            ```
2. 실전 ( 로컬버전 )
   1. 생성
   ``` python -m venv [가상환경이름] ```
   2. 활성화 
      1. (Terminal)
      ``` source [가상환경이름]/bin/activate ```
   
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







3. git 사용 시
   1. git pull 받은 상대방의 버전을 일치시키기
   ``` pip install -r requirements.txt ```

admin
models
views
settings
urls


> 흐름

<URLs>

`path('articles/', views.index)` =>

<View>

`def index(request):`
   `render render(requet, 'articles/index.html')` =>

<Template>

`articles/templates/articles/index.html`




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


## ADMIN

1. 계정 생성
> 터미널
``` python manage.py createsupersuer ```
- admin
- `Enter`
- password
- repassword


> 확인용
`python manage.py showmigrations `

> 설계도 번역본 확인 
` python manage.py sqlmigrate articles 0001 `


> 초기화
- 만든 파일 다 삭제하면 됨



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

### 조회

- views.py
```
from .models import Todo

def index(request):
   todo = Todo.objects.all()
   context = {
      'todos' : todos,
   }
   return render(request, 'todos/index.html', context)

```

- index.html
{% for article in articles %}
       <p>article : {{ article }} </p>
       <p>글 번호 :
            <a href="{% url 'articles:detail' article.pk %}">{{ article.pk }}</a>
        </p> 
       <p>article.content : {{ article.content}} </p> 
    {% endfor %}

## QuerySet API 
> 터미널
``` pip install ipython django-extensions ```

> settings.py > INSTALLED_APP 
- ` 'django_extensions', ` 입력

- 업데이트 
``` pip freeze > requirements.txt ```


안될떄

<!-- 일단 pip list 명령 대신에 python -m pip list 명령을 실행해보시고, 그 결과를 비교해보시겠어요?

그리고 라이브러리 설치도 python -m pip install django-extensions 명령으로 설치하신 후에 manage.py 명령을 수행해보시겠어요? -->

python3 manage.py shell_plus
--ipython 이거 치고
아래꺼 치기
> 터미널 
``` python3 manage.py shell_plus ```

` article = Article() `

` article.title = 'title' ` title에 값 할당

` article.content = 'django!' ` content에 값 할당

` article.save() ` 저장하기

` Article.objects.all() ` 저장되었나 확인하기

- db가서 확인하기 


<!-- 한번에 쓰기 -->
` article = Article(title='second', content='django!') `

articles에 넣기
` articles = Article.objects.all() `


<!-- 다른 방법 -->
` Article.objects.create(title='third', content='django!') `



단일 데이터 조회

` article = Article.objects.get(pk=1) `

` Article.objects.filter(content='django!') `

특정 단어로 시작하는 것 조회

` Article.objects.filter(content__startswith='dj') `

특정 단어가 들어가는 것 조회

` Article.objects.filter(content__contains='!') `

지정한 숫자보다 높은 것 조회

` Article.onjects.filter(pk__gte=3)

- 수정

article = Article.objects.get(pk=1)

article.content = '수정할 내용

article.save()


- 삭제

article.delete()

반복문
```py 
for article in articles:
   print(article)
   print(article.id) id 조회 pk로 쳐도 조회 가능
```

전체 조회

단일객체 조회

- 생성


## FORM

- articles 앱에 forms.py 파일 생성
```py
from django import forms

class ArticleForm(forms.Form):
   title = forms.CharField(max_length=10)
   content = forms.CharField()
```

- form class 를 적용한 new 로직

```py
form .forms import ArticleForm

def new(request):
   form = ArticleForm()
   context = {
      'form' : form,
   }
   return render(request, 'articles/new.html', context)
```

- articles/new.html 에 form 적용

```pyㅣ멱ㄷ
{{ form }}

```
- p tag 적용한 form

```
{{ form.as_p }}
```

- 속성을 바꾸고 싶을 때
articles/forms.py

```

content = forms.CharField(widget=forms.Textarea)

```


## ModelForm ( DB에 저장 )

- ModelForm class 선언

articles/forms.py
```py
from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
   class Meta:
      model = Article
      fields = '__all__' ( 여기에 원하는 요소 넣을 수 있음)
      (ex_1)
      fields = ('title',) > title 만 나옴
      (ex_2)
      fields = ('title','content',)
      
      exclude = ('title',) > title 만 제외시킬수 있음
```


- ModelForm create 로직

articles/views.py
```py
from .forms import ArticleForm

def create(request):
   form = ArticleForm(request.POST)
   # 통과 했을 때
   if form.is_valid():
      article = form.save()
      return redirect('articles:detail', article.pk)
   # 통과하지 못했을 때
   context = {
      'form' : form,
   }
   return render(request, 'articles/new.html', context)
```

- edit 의 value 정해주기

articles/views
```py
def edit(request, pk):
   article = Article.objects.get(pk=pk)
   form = ArticleForm(instance=article)
   context = {
      'article': article,
      'form': form,
   }
   return render(request, 'articles/edit.html', context)

```


```py

def update(request,pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/update.html', context)

```


- SAVE
articles/forms.py
```py
class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        widget=forms.TextInput(
            attrs={
                'class': 'my-title',
                'placeholder': '제목을 입력해주세요.'
            }
        )
    )
```


- NEW , CREATE 병합
articles/views.py
```py
def create(request):
    # HTTP requests method가 POST라면
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    # POST가 아니라면
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/new.html', context)
```

불필요해진 new url 제거

articles/views.py
```py
   path('new/') 삭제
```

코드 수정
articles/index.html
```html
<a href="{% url 'articles:create' %}">CREATE</a>
```
articles/create.html
```html
<h1>CREATE</h1>
<form action="{% url 'articles:create' %}" method="POST">
{% csrf_token %}
{{ form.as_p}}
</form>
```

articles/views.py
```py
def create(request):
   ...
   ...
   return render(request, 'articles/create.html', context)
```

결론 = create + new = create
      update + edit = update



## Cookie & Sessions

- 생성

accounts/urls.py
```py
from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [

]
```

crud/urls.py
``` py
urlpatterns = [
   ...,
   path('accounts/', include('accounts.urls')),
]
```

accounts/models.py  
```py
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
   pass

```

settings.py
```py

AUTH_USER_MODEL = 'accounts.User' # 기본 값 'auth.User'
```

accounts/admin.py
```py
from django.contrib.auth.admin import UserAdmin
from .models import User

admin.site.register(User, UserAdmin)
```
> 주의
프로젝트 중간에 AUTH_USER_MODEL을 변경 할 수 없음

- 데이터베이스 초기화
1. articles/migtations/ 번호붙은 친구들 삭제
2. 데이터베이스 삭제 (db.sqlite3)

다시 생성
python manage.py makemigrations
python manage.py migrate


## LOGIN
<Cookie,Sessions 와 이어서 진행>

accounts/urls.py
```py
from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
   path('login/', views.login, name='login'),
]
```

accounts/views.py
```py
from django.contrib.auth.forms import AuthenticationForm

def login(request):
   if request.method == 'POST':
      form = AuthenticationForm(request, request.POST)
      if form.is_valid():
         auth_login(request, form.get_user())
         return redirect('articles:index')

   else:
      form = AuthenticationForm()
   context = {
      'form' : form,
   }
   return render(request, 'accounts/login.html', context)
```

templates/accounts/login.html
```html
  <h1>로그인</h1>
  <form action="{% url 'accounts:login' %}" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit">
  </form>
```

articles/index.html
```html
  <a href="{% url 'accounts:login' %}">Login</a>
```


## LOGOUT
accounts/urls.py
```py
    path('logout/', views.logout, name='logout'),
```

accounts/views.py
```py
from django.contrib.auth import logout as auth_logout

def logout(request):
    auth_logout(request)
    return redirect('articles:index')
```

articles/index.html
```html
  <form action="{% url 'accounts:logout' %}" method="POST">
    {% csrf_token %}
    <input type="submit" value="Logout">
  </form>
```

- 로그인 유저 정보 출력

articles/index.html
```html
  <h3>안녕하세요, {{ user }} 님!</h3>
```


## 회원가입

accounts/urls.py
```py
   path('login/', views.login, name='login'),
   path('logout/', views.login, name='logout'),
   path('signup/', views.signup, name='signup'),

```

accounts/forms.py 생성
```py
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):
   class Meta(UserCreationForm.Meta):
      model = get_user_model()

```

accounts/views.py
```py
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import CustomUserCreationForm 

def signup(request):
   if request.method == 'POST':
      form = CustomUserCreationForm(request.POST)
      if form.is_valid():
         form.save()
         # 만약 회원가입 후 로그인까지 진행하려면
         user = form.save()
         auth_login(request, user)
         return redirect('articles:index')
   else:
      form = CustomUserCreationForm()
   context = {
      'form' : form,
   }
   return render(request, 'accounts/signup.html', context)
```

accounts/signup.html 생성
```html
<form action="{% url 'accounts:signup'%}"  method="POST">
   {% csrf_token %}
   {{form.as_p}}
   <input type="submit">
</form>
```
> migrate 한번 해주기


## 회원 탈퇴

accounts/urls.py
```py
   path('delete/', views.delete, name='delete'),
```

accounts/views.py
```py
def delete(request):
   # 유저 삭제
   request.user.delete()
   # 세션 삭제 ( 필수 아님 )
   auth_logout(request)
   return redirect('articles:index')
```

articles/index.html
```html
<form action="{% url 'accounts:delete' %}" method="POST">
  {% csrf_token %}
  <input type="submit" value="회원탈퇴">
</form>

```



## 회원정보 수정

accounts/forms.py
```py
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class CustomUserChangeForm(UserChangeForm):
   class Meta(UserChangeForm.Meta):
      model = get_user_model()
      fields = ('email','first_name','last_name',)
```   

accounts/urls.py
```py
   path('update/', views.update, name='update')
```

accounts/views.py
```py
from .forms import CustomUserCreationForm, CustomUserChangeForm

def update(request):
   if request.method == 'POST':
      form = CustomUserChangeForm(request.POST, instance=request.user) # 수정엔 instance가 들어감
      if form.is_valid():
         form.save()
         return redirect('articles:index')
   else:
      form = CustomUserChangeForm(instance=request.user)
   context = {
      'form' : form,
   }
   return render(request, 'accounts/update.html', context)
```

accounts/update.html
```html
<form action="{% url 'accounts:update' %}" method="POST">
  {% csrf_token %}
  {{ form.as_p}}
  <input type="submit">
</form>

```


## 비밀번호 변경

accounts/urls.py
```py
   path('password/', views.change_password, name='change_password'),
```

accounts/views.py
```py
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash


def change_password(request):
   if request.method == 'POST':
      form = PasswordChangeForm(request.user, request.POST)
      if form.is_valid():
         user = form.save()
         # 비밀번호 변경시 세션 무효화 방지
         update_session_auth_hash(request, user)
         return redirect('articles:index')
   else:
      form = PasswordChangeForm(request.user) # request.user 필수로 넣기
   context = {
      'form': form,
   }
   return render(request, 'accounts/change_password.html', context)

```

accounts/change_password.html 생성
```html
<form action="{% url 'accounts:change_password' %}" method="POST">
  {% csrf_token %}
  {{ form.as_p}}
  <input type="submit">
</form>
```





## 비로그인 , 로그인 화면 다르게 나타내기

articles/index.html
```html
  {% if request.user.is_authenticated %}
    <h3>안녕하세요, {{ user }} 님!</h3>
    <form action="{% url 'accounts:logout' %}" method="POST">
      {% csrf_token %}
      <input type="submit" value="Logout">
    </form>
    <form action="{% url 'accounts:delete' %}" method="POST">
      {% csrf_token %}
      <input type="submit" value="회원탈퇴">
    </form>
    <a href="{% url 'accounts:update' %}">회원정보수정</a>
  {% else %}
    <a href="{% url 'accounts:login' %}">Login</a>
    <a href="{% url 'accounts:signup' %}">Signup</a>
  {% endif %}
```

accounts/views.py
```py
def login(request):
    if request.user.is_authenticated:
        return redirect('articles:index')

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('articles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)


def signup(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)

```


## 데코레이터
- 로그인 된 사용자만 쓸 수 있도록
articles/views.py
```py
from django.contrib.auth.decorators import login_required

@login_required
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/new.html', context)


@login_required
def delete(request, artilce_pk):
    # 삭제할 데이터 조회
    article = Article.objects.get(pk=artilce_pk)

    # 조회한 데이터 삭제(DELETE)
    article.delete()

    # 전체 조회 페이지 이동
    return redirect('articles:index')


@login_required
def update(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/edit.html', context)
```


accounts/views.py
```py
from django.contrib.auth.decorators import login_required

@login_required
def logout(request):
    auth_logout(request)
    return redirect('articles:index')

@login_required
def delete(request):
    # print(dir(request.user))
    request.user.delete()
    return redirect('articles:index')

@login_required
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/update.html', context)


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            # 비밀번호 변경시 세션 무효화 방지
            update_session_auth_hash(request, user)
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/change_password.html', context)

```










## 추가경로

settings.py => TEMPLATES
'DIRS" : [기본 템플릿 경로 외에 추가 경로를 작성],
ex[ BASE_DIR / 'my_templates']



































<!-- https://www.notion.so/hg-edu/Django-4755b2b2fe6f4292959e9940f37f59b2?pvs=4

https://www.notion.so/hg-edu/Python-8a38c543b50a4eb7a796cbe9a2358e86?pvs=4

https://www.notion.so/hg-edu/Python-8f920eeebb99493fade86371c290ef19?pvs=4

https://www.notion.so/hg-edu/django-shell_plus-81da033a453842c2b816c7987cb16ad8?pvs=4
1

1. python -m venv venv
2. source venv/bin/activate
3. pip install django==3.2.18
4. pip freeze > requirements.txt
5. .gitignore
6. git init
7. django-admin startproject firstpjt.

python manage.py runserver

 -->
