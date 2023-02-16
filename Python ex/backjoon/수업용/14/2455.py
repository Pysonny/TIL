lists = []
start = 0
while True:
    try:
        p_out,p_in = list(map(int,input().split()))
        start += (p_in - p_out)
        lists.append(start)
    except:
        break
print(max(lists))