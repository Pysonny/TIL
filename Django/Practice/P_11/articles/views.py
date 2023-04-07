from django.shortcuts import render
from .models import Article


# Create your views here.
def index(request):
    # DB에 전체 게시글 조회를 요청하고 쿼리셋을 응답받아 저장
    articles = Article.objects.all()
    print(articles)
    context = {
        'articles': articles,
    }

    # context - 템플릿에 데이터와 함께 렌더링
    return render(request, 'articles/index.html', context)