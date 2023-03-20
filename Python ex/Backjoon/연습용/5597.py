lists = []
while True:
    try:
        nums = int(input())
        lists.append(nums)
        
    except:
        break
for i in range(1,31):
    if i not in lists:
        print(i)