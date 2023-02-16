lists = []
for i in range(int(input())):
    a = int(input())
    lists.append(a)

if lists.count(0) > lists.count(1):
    print('Junhee is not cute!')
else:
    print('Junhee is cute!')