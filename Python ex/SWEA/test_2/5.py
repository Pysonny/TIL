T = int(input())

for t in range(1,T+1):
    nums_0 = list(map(int,input().split()))
    result_1 = []
    result_2 = []
    cnt = 0
    for i in nums_0:
        cnt += 1
        if cnt % 2 ==1:
            result_1.append(i*2)
        else:
            result_2.append(i)
    res_all = sum(result_1) + sum(result_2)
    if res_all % 10 == 0:
        print(f'#{t} {0}')
    else:
        print(f'#{t} {10-(res_all%10)}')

        



