lists = []
for _ in range(5):
    a = int(input())
    if a < 40:
        lists.append(40)
    else:
        lists.append(a)

print(sum(lists)//len(lists))

