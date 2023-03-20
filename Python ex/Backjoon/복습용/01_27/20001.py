A = "문제"
B = "고무오리"
C = "고무오리 디버깅 끝"

cnt = []

while True:
    T = input()
    if T == A:
        cnt.append(1)
    elif T == B:
        if not cnt: # cnt 에 아무것도 없으면
            cnt.append(1)
            cnt.append(1)
        else:
            cnt.pop()
    elif T == C:
        break
if not cnt:
    print("고무오리야 사랑해")
else:
    print("힝구")