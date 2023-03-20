# pe = {}

# for _ in range(int(input())):
#     p,c = input().split()

#     if c == 'enter':
#         pe[p] = 'enter'
#     else:
#         if pe[p]:
#             del pe[p]

# for people in sorted(pe,reverse=True):
#     print(people)
            

pe = {}

for _ in range(int(input())):
    p,c = input().split()
    if p not in pe:
        pe[p]= c
    else:
        del pe[p]

for people in sorted(pe, reverse=True):
  print(people)