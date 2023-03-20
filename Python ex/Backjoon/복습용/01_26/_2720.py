T = int(input())

for t in range(1,T+1):
    money = int(input())
    li = [25,10,5,1]
    result = []
    for i in li:
        result.append(money//i)
        money=money % i 
    print(*result)
    
