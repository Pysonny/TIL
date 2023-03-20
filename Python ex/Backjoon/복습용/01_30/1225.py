# # 1
# A,B = map(int,input().split())

# result = 0
# for i in str(A):
#     for j in str(B):
#         result += int(i)*int(j)

# print(result)


# 2
# import sys
# input= sys.stdin.readline()

N , M = map(list,input().split())
N = list(map(int,N))
M = list(map(int,M))
print(N*M)