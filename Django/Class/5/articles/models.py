from django.db import models

# Create your models here.

class Article(models.Model):
    # 필드이름 = 데이터 타입(제약조건)
    title = models.CharField(max_length=10) # 길이제한 O
    content = models.TextField() # 길이제한 X

    # 추가
    created_at = models.DateTimeField(auto_now_add=True) # 기본값 = FALSE
    updated_at = models.DateTimeField(auto_now=True)

    # python manage.py makemigrations 터미널 실행
    # 1 입력
    # Enter 쳐서 진행
