# 2 달력 

T = int(input()) 

for t in range(1, T+1):
    numbers = int(input())
    for i in numbers():
        if i[0,4] == 0:
            print(f'#{t} {-1}')