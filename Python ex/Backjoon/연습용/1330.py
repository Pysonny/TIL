nums = list(map(int,input().split()))
if nums[0] > nums[1]:
    print('>')
elif nums[0] < nums[1]:
    print('<')
else:
    print('==')