nums = []
for _ in range(7):
    a = int(input())
    if a % 2 != 0:
        nums.append(a)
if len(nums) == 0 :
    print('-1')
else:
    print(sum(nums))
    print(min(nums))
