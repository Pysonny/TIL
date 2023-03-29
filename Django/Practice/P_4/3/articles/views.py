from django.shortcuts import render

# Create your views here.

def calculate(request,num1,num2):
    plus = num1 + num2
    minus = num1 - num2
    times = num1 * num2
    divide = num1 // num2
    context = {
        'plus' : plus,
        'minus' : minus,
        'times' : times,
        'divide' : divide,
    }
    
    return render(request,'articles/calculate.html', context)


def home(request):
    return render(request, 'articles/home.html')