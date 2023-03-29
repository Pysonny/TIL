from django.shortcuts import render

# Create your views here.
def number_print(request, number):
    # number = request.GET.get('number')
    lists= []
    lists.append(number)

    # 문자열 자체를 넣고 숫자를 받는식?

    Atag = f" <a href='{% url 'number_print' {num1} %}'>1</a> "

    
    context = {
        'number' : number,
        'lists' : lists,
        'Atag' : Atag,
    }
    return render(request, 'articles/number_print.html', context)


def home(request):
    
    return render(request, 'articles/home.html')
