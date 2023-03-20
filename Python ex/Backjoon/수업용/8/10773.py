# result = []

# for i in range(int(input())):
#     nums = int(input())

#     if nums == 0:
#         result.pop()
#     else:
#         result.append(nums)
# print(sum(result))


T = int(input())
result = []

for t in range(1,T+1):
    num = int(input())
    if num not in result:
        result.append(num)
    if num == 0:
        result.pop()
        result.pop()
    else:
        result.append(num)
print(sum(result))