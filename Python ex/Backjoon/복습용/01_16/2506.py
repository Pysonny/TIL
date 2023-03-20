T = int(input())
A = map(int,input().split())
plus = 0
cnt = 0
for i in A:
    if i == 1:
       cnt += 1+plus
       plus += 1
    else:
        plus = 0
print(cnt) 
