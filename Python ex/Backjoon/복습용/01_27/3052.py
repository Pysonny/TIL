li =[]
for _ in range(10):
    A = int(input())
    a = A % 42
    li.append(a)

print(len(set(li)))