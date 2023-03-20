import sys
input= (sys.stdin.readline)

T = int(input())

a = []
count = 1

for i in range(T):
    N = int(input())
    a.append(N)

# 막대기 길이를 먼저 받아서 리스트로 만든다

last = a[-1] # 마지막 막대기는 무조건 볼 수 밖에 없다

for j in reversed(range(T)): # 역순으로 하나씩 
    if a[j] > last: 
        count += 1 
        last = a[j] # 더 큰 막대기로 바뀐다
print(count)