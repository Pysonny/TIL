# import sys
# sys.stdin = open('SWEA/test_2/input.txt', "r")

T = int(input())

for t in range(1,T+1):
    N = int(input())
    for i in range(N):
        n = {}
        nums = list(map(int,input().split()))
        for num_1 in nums:
            if num_1 not in n:
                n[num_1] = 1
            else:
                n[num_1] = n[num_1]+1
        max_num = int(max(n.keys()))
        print(f'#{t} {max_num}')
            
# 컬렉션 카운터

