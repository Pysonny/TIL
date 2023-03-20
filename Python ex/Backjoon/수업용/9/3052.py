lists = []

for _ in range(10):
    T = int(input())
    a = T%42
    if a not in lists:
        lists.append(a)

print(len(lists))
