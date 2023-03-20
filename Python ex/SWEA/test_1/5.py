# 5 양 세기

T = int(input()) # 테스트 케이스 수

for t in range(1, T+1):
    num = list(range(10))
    N = int(input())
    c = 0
    j = N
    for i in num:
        if j in num:
            num.pop(j)
            c += 1