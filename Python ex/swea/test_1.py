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
    

# 2 달력 

T = int(input()) 

for t in range(1, T+1):
    numbers = int(input())
    for i in numbers():
        if i[0,4] == 0:
            print(f'#{t} {-1}')


# 3 비밀번호

P , K = list(map(int,input().split()))
t = 0
for n in range(K,1000):
    if n != P:
        t += 1
    else:
        print(t + 1)
        break


# 4 약수

N = int(input())

for n in range(1,N+1):
    if N % n == 0:
        print(n,end=" ")


# 5 양 세기

T = int(input()) # 테스트 케이스 수

for t in range(1, T+1):
    num = list(range(10))
    N = int(input())
    c = 0
    j = N
    for i in num:
        if j in num:
            num.pop(j)
            c += 1