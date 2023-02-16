# A = input()

# for i in range(len(A)):
#     for j in range(len(A)):
#         for k in range(len(A)):








a = input()
lst = []
for i in range(1, len(a)):       # 모든 경우의 수를 구한다
    for j in range(i+1, len(a)):
        first = a[:i][::-1]   # m
        second = a[i:j][::-1] # o
        third = a[j:][::-1] # letib 
        lst.append(first + second + third) # 글자수를 유지하며 반복한 모든 수를 더한다
lst.sort()
print(lst[0]) #  정렬 시 정답이 알파벳 순서상 첫번째로 나오기 때문에 [0]을 통해 출력