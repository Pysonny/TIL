#1부터 사용자가 입력한 양의 정수까지의 총합을 구하는 코드를 작성하시오

## while 문 사용
n = int(input(' 정수를 입력하세요 >'))

a = 0
result = 0

while n >= a:
    result += a
    a += 1
print(result)


## for 문 사용

n = int(input(' 정수를 입력하세요 >'))
result = 0

for a in range(1,n + 1):
    result = a + result
print(result)


## 함수사용

print(sum(range(1,int(input()+1))))


numbers = [ 1 ,2 ,3]

print(len(numbers))


## 정렬

a = [ 10 , 25 , 5]

print(sorted(a))


# map 함수

nums = ['1','2','3']
result = 0
for num in nums:
    result += int(num)
print(result)



nums = ['1','2','3']
new_nums =[]
for num in nums:
    new_nums.append(int(num))
print(new_nums)




nums = ['1','2','3']
new_nums = map(int,nums)
print(new_nums)
print(list(new_nums))



a = input()
print(a) # 2 5

b = a.split()
print(b) # '2','5'

c = map (int,b)
print(c) # map

d,e = list(c)
print(d,e) 2, 5


a =
print(a) # 2 5

b =
print(b) # '2','5'

c =
print(c) # map

d,e = list(map (int,input().split()))
print(d,e) 2, 5
