T = int(input())

li=[]
for t in range(T):
    A = int(input())
    # 요소가 있으면 실행하도록 
    if len(li) != 0:
        if A == 0:
            li.pop()
        else:
            li.append(A)
print(sum(li))


# 만약 0이 계속 나오게 될 때는 ??
# 지울게 없을 때 0이 나오게 되면 오류가 뜨는데 어떠한 방식을 써야 할까?
# pass 나 continue로는 해결이 안 됨.