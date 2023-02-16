# 2

N , X  = list(map(int,input().split()))
A = list(map(int,input().split()))

for n in A[:]:
    if n > X-1:
        A.remove(n)
    else:
        continue

print(*A)



