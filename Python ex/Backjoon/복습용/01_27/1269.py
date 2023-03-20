# x , y = map(int,input().split())

# A = list(map(int,input().split()))
# B = list(map(int,input().split()))

# C = []
# D = []
# for i in A:
#     if i not in B:
#         C.append(i)
# for j in B:
#     if j not in A:
#         D.append(j)
# print((len(C)+len(D)))
        

x , y = map(int,input().split())

A = set(list(map(int,input().split())))
B = set(list(map(int,input().split())))

print(len(A-B)+len(B-A))
