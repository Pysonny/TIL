from django.db import models

# Create your models here.

class Review(models.Model):
    # 필드이름 = 데이터 타입(제약조건)
    title = models.CharField(max_length=20) 
    content = models.CharField(max_length=200)
    movie = models.CharField(max_length=20)

class Comment(models.Model):
    # 외래 키 필드
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
