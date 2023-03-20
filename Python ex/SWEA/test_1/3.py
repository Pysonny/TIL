# 3 비밀번호

P , K = list(map(int,input().split()))
t = 0
for n in range(K,1000):
    if n != P:
        t += 1
    else:
        print(t + 1)
        break