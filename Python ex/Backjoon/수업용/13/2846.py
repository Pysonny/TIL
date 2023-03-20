# max_ = 0
# lists = []
# T = int(input())
# A = map(int,input().split())
# for i in A:
#     if max(lists) > i:
#         del lists[0]
#         Max_ = max(lists)- min(lists)
#         lists = []
#         if Max_ > max_:
#             max_=Max_
#     elif lists == False:
#         lists.append(0)
#     else:
#         lists.append(i)
# print(max_)

N = int(input())
lists = list(map(int,input().split()))
max_ = 0
max_lists= []
for i in range(N-1):
    if lists[i] < lists[i+1]:
        max_ += lists[i+1]-lists[i]
    else:
        max_lists.append(max_)
        max_ = 0
max_lists.append(max_)
print(max(max_lists))

