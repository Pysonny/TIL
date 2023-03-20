#1
li = []
for _ in range(int(input())):
    A = input()
    if A not in li:
        li.append(A)

li.sort()
li.sort(key=len)

print(*li,sep='\n')


#2
heap = []

for _ in range(int(input())):
    heap.append(input())

result_1 = set(heap)
result = list(result_1)
result.sort()
result.sort(key=len)

print(*result,sep='\n') # 리스트 한 줄 씩 출력