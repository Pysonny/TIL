from django.shortcuts import render
import random

# Create your views here.
def today_dinner(request):
    foods = ['chicken','hamburger','noodle']
    random_foods = random.choice(foods)
    context = {
        'foods' : foods,
        'random_foods': random_foods,
    }
    return render(request, 'articles/today_dinner.html',context)

def throw(request):
    return render(request, 'articles/throw.html')

def catch(request):

    data = request.GET.get('message')

    context = {
        'data': data,
    }
    return render(request, 'articles/catch.html', context)




def lotto_create(request):
    return render(request, 'articles/lotto_create.html')

def lotto(request):
    num = int(request.GET.get('number'))
    lotto_numbers = []

    numbers = list(range(1,46))
    print(numbers)
    # 숫자를 받아 그 숫자만큼 반복문 돌림
    for _ in range(num):
        lotto_numbers.append(sorted(random.sample(numbers,6)))
    context = {
        'lotto_numbers': lotto_numbers,
    }
    return render(request, 'articles/lotto.html', context)

