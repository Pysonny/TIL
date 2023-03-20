T = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

list_0=list((set(B)) ^ set(A)) # [(A-B) + (B-A)]
print(len(list_0))