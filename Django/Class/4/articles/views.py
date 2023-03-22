from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'name':'Willson',
    }
    return render(request, 'articles/index.html', context) # 모든 템플릿은 templates 안에 있어야만 한다!

def dinner(request):
    foods = ['rice','noodle','hamburger']
    context = {
        'foods' : foods,
    }
    return render(request, 'articles/dinner.html', context)


def search(request):
    return render(request, 'articles/search.html')

def throw(request):
    return render(request, 'articles/throw.html')

def catch(request):

    data = request.GET.get('message')

    context = {
        'data': data,
    }
    return render(request, 'articles/catch.html', context)