import sys
sys.stdin = open('input.txt','r')

T = int(input())

for a in range(T):
    N ,M = map(int,input().split())
    A = [list(map(int,input().split())) for _ in range(N)]
    K_ = []
    for i in range(N-M+1):
        for j in range(N-M+1):
            fly = 0
            for k in range(M):
                for l in range(M):
                    fly += A[i+k][j+l]
            K_.append(fly)
    print('#'+str(a+1),max(K_))