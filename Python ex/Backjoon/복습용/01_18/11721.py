S = input()
cnt = 0
for i in S:
    cnt+= 1
    if cnt < 10:
        print(i,end='')
    elif cnt >= 10:
        print(i,end='\n')        
        cnt = 0


