heap = []

for _ in range(int(input())):
    heap.append(input())

result_1 = set(heap) # 중복 값 빼고
result = list(result_1) # 리스트로 변환
result.sort() # 알파벳 순으로 정렬
result.sort(key=len) # 단어 길이 순으로 정렬

print(*result,sep='\n') # 리스트 한 줄 씩 출력

# sorted type => list 변환