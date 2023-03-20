matrix = [input() for _ in range(5)]

for i in range(15):
    for j in range(15):
        try:
            print(matrix[j][i],end='')
        except:
            continue 
print()


# 참고

mat = []

for _ in range(5):
    line = list(input())
    mat.append(line)
  
for i in range(max(len(a) for a in mat)):
    for j in range(5):
        if i < len(mat[j]):
            pass
            print(mat[j][i], end='')  