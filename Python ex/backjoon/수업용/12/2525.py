# N , M = map(int,input().split())
# A = int(input())

# M += A


# if M >= 60:
#     N += 1
#     M -= 60
# if N >= 24:
#     N -= 24

# if M == 60:
#     N += 1
#     M = 0
# print(N,M)


N, M = map(int, input().split())
timer = int(input()) 

# 1차 계산
N += timer // 60 
M += timer % 60

# 2차 계산
if M >= 60:
    N += 1
    M -= 60
if N >= 24:
    N -= 24

print(N,M)