
# 최고점과 최저점을 뺀 나머지 3명 점수의 최고점과 최저점의 차이가 4점 이상 나게 되면 
# 점수 조정을 거쳐서 다시 점수를 매기려고 한다. 점수를 집계하여 총점을 계산하거나, 
# 점수 조정을 거쳐서 다시 점수를 매기려고 하는 경우에는 총점 대신 
# KIN(Keep In Negotiation)을 출력하는 프로그램을 작성하시오.

min_ = 0

for _ in range(int(input())):
    N = list(map(int,input().split()))
    N.sort()
    N.pop(0)
    N.pop()
    if N[2] - N [0] >= 4:
        print('KIN')
    else:
        min_ = sum(N)
        print(min_)
    

# for _ in range(int(input())):
#     N = list(map(int,input().split()))
#     N.remove(max(N))
#     N.remove(min(N))
#     if max(N) - min(N) >= 4:
#         print('KIN')
#     else:
#         print(sum(N))

    

    
    
    