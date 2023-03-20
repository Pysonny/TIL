
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


3. git 사용 시
   1. git pull 받은 상대방의 버전을 일치시키기
   ``` pip install -r requirements.txt ```






<!-- https://www.notion.so/hg-edu/Django-4755b2b2fe6f4292959e9940f37f59b2?pvs=4

https://www.notion.so/hg-edu/Python-8a38c543b50a4eb7a796cbe9a2358e86?pvs=4

https://www.notion.so/hg-edu/Python-8f920eeebb99493fade86371c290ef19?pvs=4

https://www.notion.so/hg-edu/django-shell_plus-81da033a453842c2b816c7987cb16ad8?pvs=4


1. python -m venv venv
2. source venv/bin/activate
3. pip install django==3.2.18
4. pip freeze > requirements.txt
5. .gitignore
6. git init
7. django-admin startproject firstpjt.

python manage.py runserver
 -->
