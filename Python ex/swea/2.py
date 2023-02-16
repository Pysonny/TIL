import sys
sys.stdin = open('swea/input.txt', "r")


# 1 입력으로 주어진 문장에 모든 소문자 알파벳을 찾아 대문자로 변환한 다음,
#   그 결과를 출력하는 프로그램을 작성하라.

string = input().split()

answer = string[0].upper()
print(answer)


# 2 1부터 주어진 숫자만큼 모두 더한 값을 출력하시오.

number = int(input())

answer = 0
for n in range(1,number + 1):
    answer += n
print(answer)



# 3 가위바위보 승자 확인

a ,b = list(map(int,input().split()))

if a == 1:
    if b == 2:
        print('B')
    elif b == 3:
        print('A')
elif a == 2:
    if b == 1:
        print('A')
    elif b == 3:
        print('B')
elif a == 3:
    if b == 1:
        print('B')
    elif b == 2:
        print('A')

# 4 대각선 

a = '+++++'

for i in a:
    i = '#'     
    print(a)