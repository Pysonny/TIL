T = int(input()) # 7
que = [i for i in range(1,T+1)]
discard_cards = []
# while 반복문
while len(que) > 1:
    discard_cards.append(que.pop(0))

# Input
N = 7
# queue = [i for i in range(1, N+1)]
queue = list(range (1, N+1))
discard_cards = []
# 1장 남을때까지 반복 => while
while len(queue) › 1:
# 우선, 제일 위에 있는 카드를 바닥에 버린다.
# queue에서 제일 위 : pop(0)
    discard_cards.append (queue. pop (0))
# 그 다음, 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다.
queue. append (queue. pop (0))
print (discard_cards, queue)
# 1 3 5 7 4 2 6
print (*discard_cards, queue[0])