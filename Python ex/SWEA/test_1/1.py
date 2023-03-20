# 1 10개의 수를 입력 받아, 그 중에서 홀수만 더한 값을 출력하는 프로그램을 작성하라.

T = int(input()) 

for t in range(1, T+1):
    numbers = list(map(int,input().split()))
    n = 0
    for i in numbers:
        if i % 2 == 0:
            continue
        else:
            n += i
    print(f'#{t} {n}')