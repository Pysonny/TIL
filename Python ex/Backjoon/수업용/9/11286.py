import heapq,sys # sys 도 받아야 시간초과가 안됨

heap = []

for _ in range(int(input())):
    x = int(input()) # int(sys.stdin.readline())
    if x != 0: 
    # 0이 아닌 정수 x를 넣고
        heapq.heappush(heap , (abs(x), x )) 
        # (|x| , x) 값을 리스트에 넣어 절대값 순으로 정렬한다
    else:
    # x가 0일 때
        try:
            print(heapq.heappop(heap)[1])
            # 절대값이 가장 작은 값{(|x| ,x )중에서 x값} 을 출력하고 배열에서 제거한다.
        except:
            print(0)
            # 배열이 비어있을 경우 0을 출력해 에러를 방지한다        