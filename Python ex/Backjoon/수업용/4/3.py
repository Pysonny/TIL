# x,y 좌표는  x 두개 y 두개
# 딕셔너리 써야할 듯





















X = []
Y = []
for comma in range(3):
    x, y = map(int, input().split())
    X.append(x)     # X 사각형
    Y.append(y)     # Y 사각형
for C in [X, Y]:    # X, Y를 따로 받음
    if 2 == C.count(C[0]):      # 같은 수가 2개 이상 있는 수를 걸러냄
        i = C[0]        # 임의의 수를 지정하지 않으면 먼저 지워지는 수 때문에 알맞는 수가 나오지 않음.
        C.remove(i)     
        C.remove(i)
    elif 2 == C.count(C[1]): 
        i = C[1]
        C.remove(i)
        C.remove(i)
print(X[0], Y[0])