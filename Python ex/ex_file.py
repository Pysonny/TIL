# # while  True:
# #     try:
# #         a = int(input())
# #         if a > 0:
# #             if a % 2 == 0:
# #                 print('True')
# #             else:
# #                 print('False')
# #         else:
# #             print('False')
# #     except:
# #         break



# # while True:
# #     try:
# #         a = int(input())
# #         if 0 <= a <= 100:
# #             if a > 60:
# #                 print('합격')
# #             else:
# #                 print('불합격')
# #         else:
# #             print('에러')
# #     except:
# #         break

# a= input()

# for i in a[::-1]:
#     print(i)

# n,m = map(int,input().split())
# if n != m:
#     if n > m :
#         n,m = m,n
#     for i in range(n+1,m,2):
#         print(i)
# else:
#     print('False')

# from collections import Counter

# a = input()
# counter = Counter(a)
# for i in counter:
#     print(i,counter[i])

s = input()
character_count = {}
    

for character in s:

    if character not in character_count:
        character_count[character] = 1
    
    else:
        character_count[character] += 1

print(character_count)

