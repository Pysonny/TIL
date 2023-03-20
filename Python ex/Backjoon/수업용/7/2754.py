grade = input()
score = 0
n1 = grade[0]
n2 = grade[1]

if n1 == 'A':
    score += 4
elif n1 == 'B':
    score += 3
elif n1 == 'C':
    score += 2
elif n1 == 'D':
    score += 1
elif n1 == 'F':
    score += 0

if not n2:
    score += 0.0
elif n2 == '+':
    score += 0.3
elif n2 == '0':
    score += 0.0
elif n2 == '-':
    score -= 0.3
else:
    score += 0.0

print(score)




