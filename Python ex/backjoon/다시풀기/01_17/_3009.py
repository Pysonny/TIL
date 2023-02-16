x = []
y = []
x_4 = 0
y_4 = 0
for _ in range(3):
    a,b = map(int,input().split())
    x.append(a)
    y.append(b)
for i in x:
    if x.count(i) == 1:
        x_4 += i
for j in y:
    if y.count(j) == 1:
        y_4 += j
print(x_4 , y_4)
