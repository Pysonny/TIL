T = int(input())

for t in range(1,T+1):
    a ,b = input().split()
    a = int(a)
    for i in b:
        print(i*a,end='')
    print()

    