T = int(input())
cards = list(range(1,T+1))

while len(cards) > 1: # 카드 리스트 개수가 1개만 남을 때 종료
    print(cards.pop(0),end=' ') # 처음(1)껄 버리고 
    cards.append(cards.pop(0)) # 두번째(2)를 맨 뒤로 추가
print(cards[0])
