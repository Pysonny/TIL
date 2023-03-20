# from collections import Counter 
# lists = []
# while True:
#     try:
#         a = int(input())
#         lists.append(a)
#     except:
                
#         print(sum(lists)//len(lists))

numbers = [int(input()) for _ in range(10)]
print(sum(numbers)//len(numbers))
print(max(numbers,key = numbers.count)) # 최빈값 구하기 
    
        
from collections import Counter
lst = []
for i in range(10):
    a = int(input())
    lst.append(a)
counter = Counter(lst)
most = counter.most_common(2)

print(sum((lst))//10)
print(most[0][0])