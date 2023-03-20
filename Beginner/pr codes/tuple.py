# result = divmod(4,3)
# print(result)
# print(type(result))

# my_dict = {'name' : '더 글로리', 'cast' : ' 송혜교'}
# print(my_dict.keys())
# print(my_dict.items())
# print(type(my_dict.items()))

# for a in my_dict.items():
#     print(a)
#     print(type(a))




# 중복된 값 빼기
locations = ['서울','서울','대전','광주','서울','대전','부산','부산']

result =[]

for location in locations:
    if location not in result:
        result.append(location)

print(result)
print(len(result))
print(set(locations))
print(len(set(locations)))


# 문자열

# 1,5,3 출력

result = [ '1','5','3']

text = ''
for elem in result:
    text = text + elem
print(text)

print(''.join(result))

print(' ',join(result))


# 리스트
