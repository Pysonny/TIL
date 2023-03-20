# dict = {
#     '1':'',
#     '2':'ABC',
#     '3':'DEF',
#     '4':'GHI',
#     '5':'JKL',
#     '6':'MNO',
#     '7':'PQRS',
#     '8':'TUV',
#     '9':'WXYZ',
#     '0':''
# }
# cnt =0
# str_1 = input()
# for d in dict.values():
#     for f in str_1:
#         if d in f:
#             cnt += int(dict.keys(d))
    
dict = {
    'ABC':3,
    'DEF':4,
    'GHI':5,
    'JKL':6,
    'MNO':7,
    'PQRS':8,
    'TUV':9,
    'WXYZ':10
}
cnt = 0
str_1 = input()
for d in dict.keys():
    for f in str_1:
        if f in d:
            cnt += dict[d]
print(cnt)