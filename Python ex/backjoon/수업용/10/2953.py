# matrix = []

# while len(matrix) <5:
#     score = list(map(int,input().split()))
#     matrix.append(score)
# A = max(sum(int(matrix())))
# print()

a = [sum(list(map(int,input().split()))) for i in range(5)]
# split()은 str형식으로 리스트에 저장됨
print(a.index(max(a))+1,max(a))
# 최대값의 위치(인덱스)+1 , 최대값