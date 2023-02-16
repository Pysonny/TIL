S = ['baekjoononlinejudge', 'startlink', 'codeplus', 'sundaycoding', 'codingsh']

words = ['baekjoon', 'codeplus', 'codeminus', 'startlink', 'starlink', 'sundaycoding',
'codingsh', ' codinghs', 'sondaycoding', 'startrink', 'icerink']

# # 리스트 탐색
# cnt = 0

# for word in words:
#     if word in S:
#         cnt += 1
# print(cnt)

# set 탐색
cnt = 0

S = set(S)
for word in words:
    if word in S:
        cnt += 1
print(cnt)

# 리스트는 다 돌아야 하지만 set에서는 index처럼 필요조건만 찾기 때문에 시간 단축이 된다.
# 메모리 함량이 적다

# set 연산
print(len(set(S) & set(words))) # 교집합 사용! for 문 사용안해도 괜춘