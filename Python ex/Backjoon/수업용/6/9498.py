score = int(input())

if score < 60:
    print('F')
elif score > 89:
    print('A')
elif score > 79:
    print('B')
elif score > 69:
    print('C')
else:
    print('D')