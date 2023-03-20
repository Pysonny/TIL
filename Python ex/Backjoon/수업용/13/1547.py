T = int(input())

lists = [1,2,3]

for _ in range(T):
    a,b = map(int,input().split())

    a1 = lists.index(a)
    b1 = lists.index(b)

    lists[a1] , lists[b1] = lists[b1] , lists[a1]

print(lists[0])