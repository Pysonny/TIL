L = []

for i in range(9):
    N = int(input())
    L.append(N)

M = max(L)
print(M)
print(L.index(M)+1)