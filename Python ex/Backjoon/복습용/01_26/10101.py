A = int(input())
B = int(input())
C = int(input())

# 180이 아닌 경우
if A + B + C != 180:
    print("Error")
# 기본적으로 합이 180 일 때
else:
    # 두 각이 같을 때
    if A==B==C == 60:
        print('Equilateral')
    elif A==B or B==C or A==C:
        print('Isosceles')
    else:
        print('Scalene')

        