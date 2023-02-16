# 1 

total = 0
for i in range(5):
    number = int(input())
    if number < 40:
        total += 40
    else:
        total += number
    
print(total // (i+1))