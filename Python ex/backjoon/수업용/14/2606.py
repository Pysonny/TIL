counts = int(input())
lists = [[],[]]

for i in range(int(input())):
    n1 , n2 = list(map(int,input().split()))

    if n1 not in lists[i]:
        lists[i].append(n1,n2)