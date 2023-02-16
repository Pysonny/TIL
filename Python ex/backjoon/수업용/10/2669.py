# 1,1 면적마다 1로 표시해서 0과 1로 구분
# 범위 설정해서


# matrix = [[0] * 100 for _ in range(100 + 1)]
# cnt = 0
# for i in range(4):
#     x, y, x1, y1 = map(int, input().split())
#     for i in range(x, x1):
#         for j in range(y, y1):
#             if matrix[i][j] == 0:
#                 matrix[i][j] += 1
#                 cnt += 1
# print(cnt)


paper = [[0 for _ in range(101)] for _ in range(101)]

for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    
    #사각형 부분만 1로 바꾸어줌
    for i in range(x1, x2):
        for j in range(y1, y2):
            paper[i][j] = 1

answer = 0
for row in paper:
    answer += sum(row)
print(answer)