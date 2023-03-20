for t in range(1,int(input())+1):
    N, K = map(int,input().split())
    A = list(map(int,input().split()))
    a = []
    for i in range(1,N+1):
        if i not in A:
            a.append(i)
    b = tuple(a)
    print(f'#{t}',*b)