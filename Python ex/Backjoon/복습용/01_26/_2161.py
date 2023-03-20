T = int(input())
li = list(range(1,T+1))

# 리스트에 남은 숫자가 한개일 때 까지
while len(li) > 1:
    # 리스트 맨 앞에 숫자를 빼준다
    print(li.pop(0),end=" ")
    # 빼준 맨 앞 숫자를 맨 뒤로 보낸다
    li.append(li.pop(0))
# 마지막에 남게 되는 카드를 출력
print(li[0])
