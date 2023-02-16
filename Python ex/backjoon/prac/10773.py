# T = int(input())
# lists = []
# for t in range(1,T+1):
#     JH = int(input())
#     lists.append(JH)
#     if JH == 0:
#         lists.pop()
#         lists.pop()
# print(sum(lists))


# 2
numbers = [3,0,4,0]
stack = []
# 로직(순회)
for number in numbers:
    # 0이면 스택에서 꺼내버리고
    if number == 0:
        stack.pop()
    # 아니면 스택에 추가한다.
    else:
        stack.append (number)
print (sum (stack))