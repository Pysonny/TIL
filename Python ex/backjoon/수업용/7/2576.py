# n_list = []
# for i in range(7):
#     n = int(input())
#     if n % 2 != 0:
#         n_list.append(n)
#         cnt += 1
#     elif cnt == 0: 
#         print('-1')

# print(sum(int(n_list)))
# print(min(int(n_list)))
lists = []
for i in range(7):
    a = int(input())
    if a % 2 != 0:
        lists.append(a)
if lists :
    print(sum(lists))
    print(min(lists))
else:
    print('-1')
    
    