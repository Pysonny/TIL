T = int(input())

for t in range(1,T+1):
    n = {}
    lenth = list(map(int,input().split()))
    
    for i in lenth:
        if i not in n:
            n[i] = 1
        else:
            n[i] = n[i] +1
    for m in n.values():
        if m == 1:
            d = n[m] # 1개나온 값의 key를 반환해서 d값 알아내고싶다 
    print(f'#{t} {d}')
