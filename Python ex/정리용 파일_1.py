# 정수형 숫자 입력
a = int(input())

# 문자열 입력
a = input()

# 띄어쓰기
print( 'it is' , a)

# 붙혀쓰기
print( 'it is' + a)

# 프린트 입력받은 거 넣기
print('저의 이름은 ',name, '이고, 올해 나이는 ',age,'세 입니다.')

print(f'저의 이름은 {name} 이고, 올해 나이는 {age}세 입니다.')

# 사칙연산
print('더하기 연산 :', number1 + number2)
print('빼기 연산 : ' , number1 - number2)
print('곱하기 연산 :', number1 * number2)
print('몫 연산 :', number1 // number2)
print('나머지 연산 :', number1 % number2)

# 리스트 객체에 저장
print([num1,num2,num3,num4,num5])

# 리스트를 일반 정수형으로
print(*a)

# for 문
a = "hello"
for i in a:
    i = (h,e,l,l,o) # 하나씩 입력받는다

# 가로로 출력
print(a,end=' ')

# 1번부터 번호지정
for index,value in enumerate(a,start =1):

# 범위
for i in range(a)
for i in range(1,a)
for i in range(1,a,2)

# index 넣어서 순서넣기
list_variable = [6, 5, 4, 3, 2, 1, 0] 

for index, element in enumerate(list_variable):
    print(index, element) # index = 0번째 element = 6  => 0 6


# 멈춤기능
    break

# 패스하고 진행
    continue

# if 
if
elif
else

# 거꾸로 출력
for element in string[::-1]:

#두 정수 오름차순 출력
if a > b:
    for num in range( b + 1, a ):
        print(num)
elif a < b:
    for num in range( a + 1 , b ):
        print(num)

# 두 정수 내림차순 출력
if a>b:
    for num in range(a -1, b, -1):
        print(num)
elif a<b:
    for num in range(b -1, a, -1):
        print(num)

# 구구단
for i in range(2,10):
    for j in range(2,10):
        print(f'{i} x {j}= {i*j}')

# list 문법
a.append(5) # 5 추가
a.pop() # 리스트 마지막 빼기
len(a) # 요소 개수
a[n] # 요소 위치
a[2:] # 2부터 끝까지
a.reverse() # 순서 뒤집기
a.sort() # 정렬
sorted(a) #정렬된 a를 불러옴
a.index(b) #a에서 b의 위치
''.join(a) #''사이에 a요소 넣어서 합침

# 리스트 정수 더하기
print(sum(list_a))

# 정수 1개 입력 받기
number = int(input())

# 공백으로 구분된 여러개의 정수 입력 받기
numbers = list(map(int,input().split()))

# 공백으로 구분된 여러개의 단어 입력 받기
string = input().split()

# 공백으로 구분된 2개의 정수 입력 받기
a, b = list(map(int,input().split()))

# 입력 줄 수가 주어지는 입력 받기
N = int(input()) # 입력 줄 수
for _ in range(N):

# 테스트 케이스와 입력 줄 수가 주어지는 입력 받기
T = int(input()) # 테스트 케이스 수
for t in range(1, T+1):
    N = int(input()) # 입력 줄 수
    for _ in range(N):

# 리스트 개수만큼 출력
for i in range(len(a)):
    print(a[i])

# 리스트 슬라이싱
a[1] # a 리스트 2번째 요소
a[1:4] # a 리스트 2번째부터 4번째까지
a[:] # a 리스트 맨 앞부터 맨끝까지
a[:3] # a 리스트 맨 앞부터 3번째까지

w = int(len(a)/2) # 리스트 반으로 나눠서
a[:w] # a 리스트 절반으로 나누기

a[-2:] # a 리스트 맨 뒤부터 2개
a[-5:-1] # a 리스트 맨 뒤에서 2번째 부터 맨 뒤에서 

# 리스트 삭제
del(a[1])
del(a[1:4]) # a 리스트 2번째부터 4번째까지 삭제

# 리스트 값 추가
a.insert(0,'x') # a 리스트 0번째 위치에 x 추가

# 리스트 내 in , not in
{'a' in a} # 있으면 True , False 

# 출력방식
end ='' # 줄 마지막에만 들어감
sep ='' # , 사이마다 다들어감 요소마다

# 딕셔너리 값 중복 개수구하기
n = {}
for num_1 in nums:
            if num_1 not in n:
                n[num_1] = 1
            else:
                n[num_1] = n[num_1]+1

# 날짜 구하기
import datetime
print(str(datetime.datetime.now())[:10])

# 범위가 정해지지 않은 조건 구하기
while True:
    try:
        a , b = map(int,input().split())
        print(a+b)
    except:
        break

# 주어진 범위 안에서 최대값 구하기
a = [sum(list(map(int,input().split()))) for i in range(5)]
print(a.index(max(a))+1,max(a))

# 이차원 리스트
matrix=[
    [1,2,3,4],
    [5,6,7,8],
    [9,0,1,2]
]
# 이중 for문을 이용한 행 우선 순회
for i in range(3):
    for j in range(4)
        print(matrix[i][j],end=' ')
    print()

# 다른방법
N = len(matrix) # 리스트의 개수
M = len(matrix[0]) # 리스트 안에 리스트의 개수
for i in range(N): 
    for n in matrix[i]:
        print(n,end= " ")  
    print() # 엔터 기능

# 이중 for문을 이용한 열 우선 순회

for i in range(4):
    for j in range(3):
        print(matrix[j][i],end=' ')
    print()

# 이중 for문의 총합
count = 0
for elem in matrix:
    count += sum(elem)
print(count)

# 다른 방법
print(sum(map(sum,matrix)))

# 최대값
max_value = 0

for i in range(3):
    for j in range(4):
        if matrix[i][j] > max_value:
        # 최소값
        # if matrix[i][j] < min_value:
            max_value = matrix[i][j]
print(max_value)

# 리스트 전치 (행 , 열 바꾸기)
transposed_matrix = [[0] * 3 for _ in range(4)]

for i in range(4):
    for j in range(3):
        transposed_matrix[i][j] = matrix[j][i] # 행, 열 맞바꾸기


# 리스트 회전하기

n =3
rotated_matrix = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        # 왼쪽으로 90도 회전
        rotated_matrix[i][j] = matrix[j][n-i-1]
        # 오른쪽으로 90도 회전
        rotated_matrix[i][j] = matrix[n-j-1][i]

# 최빈값 구하기
print(max(numbers,key = numbers.count)) # 최빈값 구하기 

# N * N 행렬 
from pprint import pprint

N = 7
graph = [[0] * N for _ in range(N)]

pprint(graph)
## N 이 주어지지 않으면 set사용

# 리스트 컴프리헨션

a = list()
 
for x in range(0, 10):
    if x % 2 == 0:
        a.append(x)
 
print(a)
# 위의 문장을 한줄로 바꾸면

a = [x for x in range(0, 10) if x % 2 == 0]
 
print(a)


# 역순 정렬
a.sort(reverse=True)