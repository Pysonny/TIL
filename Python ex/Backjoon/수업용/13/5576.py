W = []
K = []

Colleage = [W,K]

for i in Colleage:
    for j in range(10):
        score = int(input())
        i.append(score)
    i.sort()
    a = sum(i[-3::])
    print(a)


