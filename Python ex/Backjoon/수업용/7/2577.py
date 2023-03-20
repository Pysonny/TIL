# import math

# a_list = []
# for i in range(3):
#     a = int(input())
#     a_list.append(a)

# a_m = math.prod(a_list)

# for i in range(10):
#     print(a_m.count(str(i)))

a = int(input())
b = int(input())
c = int(input())
result = list(str(a * b * c))

for i in range(10):
    print(result.count(str(i)))