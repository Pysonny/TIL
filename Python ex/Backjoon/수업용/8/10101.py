a = int(input())
b = int(input())
c = int(input())

if a+b+c == 180:
    if a == b == c == 60:
        print('Equilateral')
    elif a == b or a == c or b == c:
        print('Isosceles')
    else:
        print('Scalene')
else:
    print('Error')


# count 사용해서 60 3개 찾기
# len(set(a)) == 2 (두 숫자 같을 때)
# len(set(a)) == 3 (세 숫자가 다 다를 때)
