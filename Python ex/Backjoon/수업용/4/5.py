# 답
a = int(input())
b = a
cycle = 1
while True:
    x = b//10
    y = b%10
    mix = x + y
    b = (y*10)+(mix%10)
    if b == a:
        break
    else:
        cycle += 1
print(cycle) 