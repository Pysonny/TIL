N = int(input())
LS_N = [] 
cnt = 0
while True:
    if N in LS_N:
        break
    else:
        LS_N.append(N)
        a = N // 10
        b = N % 10
        if a+b < 10:
            N = 10*b + (a+b)
            cnt += 1
        else:
            N = 10*b + ((a+b)%10)
            cnt +=1
        
print(cnt)