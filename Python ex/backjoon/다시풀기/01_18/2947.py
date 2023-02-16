A = list(map(int,input().split()))

while True:
    for i in range(4):
        if A[i+1] < A[i]:
            A[i] , A[i+1] = A[i+1] , A[i]
            print(*A)
    if A == [1,2,3,4,5]:
        break


