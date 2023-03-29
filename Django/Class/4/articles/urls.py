from django.urls import path
# 명시적 상대경로 (django 권장사항))
from . import views

app_name = 'articles'
urlpatterns = [

    # path('articles/<int:num>/', views.detail),
    # 연결해줘서 articles/ 가 필요없음
    path('index/', views.index, name='index'),
    path('<int:num>/', views.detail),
    path('<str:name>/', views.greeting),

]
