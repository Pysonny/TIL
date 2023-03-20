T = int(input()) 


for t in range(1,T+1):
    sen = input().split()
    sen2 =[]
    for i in sen:
        i = i[::-1]
        sen2.append(i)
    print(*sen2)
