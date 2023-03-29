from django.db import models

# Create your models here.

class Article(models.Model):
    content = models.CharField(max_length=80)
    completed = models.BooleanField(default=False)
    priority = models.IntegerField(default=3)
    
    # auto_now : 데이터가 저장될 때 마다 자동으로 현재 날짜시간을 저장
    # auto_now_add : 데이터가 처음 생성될 때만 자동으로 현재 날짜시간을 저장
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True)

    category = models.CharField(max_length=20)

    