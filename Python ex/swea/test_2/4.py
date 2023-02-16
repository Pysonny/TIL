T = int(input())

for t in range(1,T+1):
    str1 = input()
    str2 = str1[::-1]
    result =''
    for i in str2:
        if i == 'q':
            result = 'p' + result
        elif i == 'p':
            result = 'q' + result
        elif i == 'b':
            result = 'd' + result
        elif i == 'd':
            result = 'b' + result
    print(f'#{t} {result[::-1]}')
        