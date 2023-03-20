for t in range(int(input())):
    a =input()
    while '()' in a:
        a = a.replace('()','')
    if len(a) == 0: 
        print('YES')
    else: 
        print('NO')