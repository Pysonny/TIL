# redirect 추가
from django.shortcuts import render, redirect
from .models import Article
# Create your views here.

def index(request):
    articles = Article.objects.all()
    context = {
        'articles' : articles,
    }
    # 이동 URL 반환
    # return redirect("articles:index")

    # context - 템플릿에 데이터와 함께 렌더링
    return render(request, 'articles/index.html', context)

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article' : article,
    }
    return render(request, 'articles/detail.html', context)

def new(request):
    # form
    form = ArticleForm()
    context = {
        'form' : form,
    }
    return render(request, 'articles/new.html', context)

def create(request):
    # title = request.POST.get('title')
    # content = request.POST.get('content')

    form = ArticleFrom(request.POST)
    if form.is_valid():
        article = form.save()
        return redirect('articles:detail', article.pk)
    context = {
        'form' : form,
    }
    return render(request, 'articles/new.html', context)
    # article = Article(title=title, content=content)
    # article.save()


def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()

    return redirect('articles:index')

def edit(request,pk):
    article = Article.objects.get(pk=pk)

    context = {
        'article' : article
    }
    return render(request, 'articles/edit.html', context)

def update(request, pk):
    article = Article.objects.get(pk=pk)
    
    title = request.POST.get('title')
    content = request.POST.get('content')

    article.title = title
    article.content = content

    article.save()

    return redirect('articles:detail', article.pk)

