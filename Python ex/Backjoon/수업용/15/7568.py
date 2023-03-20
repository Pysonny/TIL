T = int(input())
a = []

for i in range(T):
    x,y = map(int,input().split())
    a.append((x,y))

for j in a:
    nums = 1 
    for k in a:
        if j[0] < k[0] and j[1] < k[1]: 
            # 몸무게 , 키 둘 다 커야할 때만 + 해준다
            nums += 1
    print(nums,end=' ')
