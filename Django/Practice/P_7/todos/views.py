from django.shortcuts import render
from .models import Todo
# Create your views here.

def index(request):
    todos = Todo.objects.all()
    context = {
        'todos' : todos , 
    }
    return render(request, 'todos/index.html', context)


def detail(request, pk):
    todo = Todo.objects.get(pk=pk)
    context = {
        'todo' : todo,
    }
    return render(request, 'todos/detail.html', context)


def new(request):
    
    return render(request, 'todos/new.html')


def create(request):
    # new 에서 보낸 사용자 데이터를 받음
    title = request.GET.get('title')
    content = request.GET.get('content')
    # completed = request.GET.get('completed')
    priority = request.GET.get('priority')
    created_at = request.GET.get('created_at')
    deadline = request.GET.get('deadline')
    
    # 받은 데이터를 DB에 저장

    Todo.objects.create(title=title,content=content,priority=priority,created_at=created_at,deadline=deadline)
    # 
    # 결과 페이지 반환
    return render(request, 'todos/create.html')