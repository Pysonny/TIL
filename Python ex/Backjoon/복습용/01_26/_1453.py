T = int(input())
# PC방 자리
PC = [0] * 101

nums = list(map(int,input.split()))
cnt = 0
for i in nums:
    # 이미 자리가 차있으면
    if PC[i] != 0:
        cnt += 1
    # 자리가 없으면 앉는다
    else:
        PC[i] += 1

print(cnt)