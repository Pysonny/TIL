from django.contrib import admin
# 우리가 가져온 클래스를 import 해야함
from .models import Article


# Register your models here.
# admin site에 등록하겠다 
admin.site.register(Article)