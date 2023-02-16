N , M = map(int,input().split())

C = list(map(int,input().split()))

Max = 0

lists = []

for i in range(N):
    for j in range(N):
        if j == i:
            break
        for k in range(N):
            if k == j or k == i:
                break
            sum_cards = C[i] + C[j] + C[k]
            
            if Max < sum_cards <= M:
                Max = sum_cards
            
            if sum_cards == M:
                break
print(Max)

