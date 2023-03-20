T = int(input())
# PC = list(range(1,101))
PC = [0] * 101 # 좌석 만들어 놓고
nums = list(map(int,input().split()))
cnt = 0
for i in nums:
    if PC[i] != 0: # 자리있으면
        cnt += 1 # 있는자리 카운트
    else:
        PC[i] += 1 # 자리 없으면 +1
print(cnt)