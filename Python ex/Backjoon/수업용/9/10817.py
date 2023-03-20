import heapq

T = list(map(int,input().split()))
heapq.heapify(T)
heapq.heappop(T)

print(T[0])