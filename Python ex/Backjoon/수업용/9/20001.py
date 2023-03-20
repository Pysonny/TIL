A = '고무오리 디버깅 시작'
B = '문제'
C = '고무오리'
D = '고무오리 디버깅 끝'

# cnt = 0

# while True:
#     T = input()
#     if T == B:
#         cnt += 1
#     elif T == C:
#         cnt -= 1
#     elif T == D:
#         break
# if cnt == 0:
#     print('고무오리야 사랑해')
# else:
#     print('힝구')


cnt = []

while True:
    T = input()
    if T == B:
        cnt.append(1)
    elif T == C:
        if not cnt: # cnt에 아무것도 없으면
            cnt.append(1)
            cnt.append(1)
        else:
            cnt.pop()
    elif T == D:
        break
if not cnt:
    print('고무오리야 사랑해')
else:
    print('힝구')