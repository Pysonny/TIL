import pprint
matrix = []
for _ in range(8):
    text = '.F.F...F'
    matrix.append(list(text))

pprint.pprint(matrix)

matrix = [list(input()) for _ in range(8)]


# 3X3

matrix = [list(map(int,input().split())) for _ in range(3)]

# N x M 입력

n,m =  map(int,input().split())
matrix=[list(map(int,input().split()))for _ in range(n)]
