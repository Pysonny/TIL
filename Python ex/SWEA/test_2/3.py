# T = int(input())

# for t in range(1,T+1):
#     N = int(input())
#     for i in range(1,N+1):
#         nums = list(map(int,input().split()))
#         cnt = 0
#         total_nums = sum(nums)
#         abs_nums = total_nums / N
#         for k in nums:
#             if k <= abs_nums:
#                 cnt += 1
#         print(f'#{i} {cnt}')

# T = int(input())

# for t in range(1,T+1):
#     N = int(input())
#     for i in range(N):
#         nums = list(map(int,input().split()))
#         cnt = 0
#         total_nums = sum(nums)
#         abs_nums = total_nums // N
#     for k in nums:
#         if k <= abs_nums:
#             cnt += 1
#         print(f'#{t} {cnt}')



T = int(input())

for t in range(1,T+1):
    N = int(input())
    nums = list(map(int,input().split()))
    cnt = 0
    total_nums = sum(nums)
    abs_nums = total_nums / N
    for k in nums:
        if k <= abs_nums:
            cnt += 1
    print(f'#{t} {cnt}')