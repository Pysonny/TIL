from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'articles/index.html')


def detail(request, num): # url 에서 정한 변수명이 request, ??? 와 동일해야함
    context = {
        'num' : num,
    }
    return render(request, 'articles/detail.html', context)



def greeting(request, name): # url 에서 정한 변수명이 request, ??? 와 동일해야함
    context = {
        'name' : name,
    }
    return render(request, 'articles/greeting.html', context)