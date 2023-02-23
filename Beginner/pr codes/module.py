# 로또 추첨 번호

import random


for i in range(5):
    numbers = range(1,46)
    lucky_numbers = random.sample(numbers,6)
    print(sorted(lucky_numbers))



print(sorted(random.sample(numbers,6)))


# 현재 날짜

import datetime
print(datetime.datetime.now()) # 2023-01-05
print(datetime.date(2023,1,5)) # 2023-01-05
print(today) # 2023-01-05
print(type(today)) # < class 'datetime.date'
print(today.year) # 2023
print(today.day) # 5

end = datetime.date(2023,6,13)
print(f'남은 시간' {end - today})  # 몇일 남았는지?



# os 변경

import OSError
print(os.listdir())