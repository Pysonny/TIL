# 딕셔너리
- 키 - 값 쌍으로 이루어진 모음
- 변경 가능하며 , 반복 가능함
```
student = {
    '홍길동' : 30 , 
    '김철수' : 25
}

for name in student: # name 은 변수의 이름
    # 키 순회
    print(student)
    # 값 순회
    print(student[name])
```
# 모듈
> 모듈
- 다양한 기능을 하나의 파일로 모여있는 것
- 특정 기능을 하는 코드를 파이썬 파일 단위로 작성한것

> 패키지
- 특정 기능에 관련된 여러 모듈의 집합
- 패키지 안에 또 다른 서브 패키지를 포함

> 코드
``` 
import random

print(random.choice(['A','B','C'])) 
# 랜덤으로 리스트 중 하나를 선택해 줌

```

```

import random
r = 0
while  
code = [1: 46]
print(random.choice(code))
```

> sort,sorted 차이점

``` 
.sort() : 메서드
# 해당 리스트 자체를 정렬

numbers = [10,2,5]
result = numbers.sort()
print(result) # None
print(numbers)

sorted() : 함수

numbers = [10,2,5]
result = sorted(numbers)
print(result) # [2,5,10]
print(numbers) # [2,5,10]

## sort 는 원문을 정렬한다면
    sorted는 수정본을 만들어 정렬하는 느낌?

```

## 파이썬 패키지

% pip install request # 터미널에 request 설치코드

## 에러/예외 처리
- 발생하는 경우
  - 해당 하는 위치를 찾아 메시지를 해결

- 로직 에러가 발생하는 경우
  - 명시적인 에러 메세지 없이 예상과 다른 결과가 나온 경우
    - 정상적으로 동작하였던 코드 이후 작성된 코드를 생각해봄
  - 확인
    - branches
      - 모든 조건이 원하는대로 동작하는지
    - for loops
      - 반복문에 집입하는지, 원하는 횟수만큼 실행되는지
    - while loops
      - for loops와 동일, 종료조건이 제대로 동작하는지
    - function
      - 함수 호출시, 함수 파라미터 , 함수 결과
  - 에러
    - 문법 에러 (Syntax Error)

---

# 튜플
- 불변한 값들의 나열
- 변경 불가능하며 , 반복 가능함
  - list = 변경 가능

# 세트
- 유일한 값들의 모음
- 순서가 없고 중복된 값이 없음.
- 변경 가능하며 , 반복 가능함
- .add , .remove 사용