for i in range(int(input())):
    C = int(input())
    d = [25,10,5,1]
    l = []
    for n in d:
        l.append(C//n)
        C = C %n
    print(*l)


# T = int(input())

# for t in range(1,T+1):
#     Q = 0
#     D = 0
#     N = 0
#     P = 0
#     a = int(input())
#     if a // 100 > 0:
#         Q += a // 25
#         a = a - (25*Q)
#     if a // 10 > 0:
#         D += a // 10
#         a = a - (10*D)
#     if a // 5 > 0:
#         N += a // 5
#         a = a - (5*N)
#     else:
#         P += a
#     print(f'{Q} {D} {N} {P}')


            



    