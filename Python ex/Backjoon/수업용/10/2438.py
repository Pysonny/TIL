# T = int(input())

# for i in range(1,T+1):
#     print('*'* i)

matrix = []

for i in range(int(input())):
    matrix.append('*'*(i+1))
print(*matrix,sep='\n')