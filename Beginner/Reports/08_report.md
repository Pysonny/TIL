# 객체와 타입
- 객체 지향 프로그래밍
  - 객체들의 모임 , 각각의 객체가 메시지를 주고받고 데이터를 처리함
- 예시
  - 사각형 (클래스)
  - 각 사각형 (인스턴스)
  - 사각형의 정보 (속성)
  - 사각형의 행동 (메소드)
- class , def
- 장점
  - 프로그램을 유연하고 변경이 용이하게 만듬
  - 소프트웨어 개발과 보수를 간편하게
- 클래스
  - 정의
    - class Myclass:
  - 인스턴스 생성
    - my_instance = Myclass()
  - 메서드 호출
    - my_instance.my_method()
  - 속성
    - my_instance.my_attribute
- 클래스 : 객체들의 분류(class)
- 인스턴스 : 하나하나의 실체

- 인스턴스
  - self

## 클래스

- 클래스 메소드
  - 클래스가 사용할 메소드
  - @classthod
    - 호출 시 , 첫번째 인자로 cls가 전달됨
  ```
  class Myclass

    @classmethod
    def class_method(cls,arg1,...)

  메소드 정리
