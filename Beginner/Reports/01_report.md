# 마크다운

## 코드블록 

> Fended Code block
- backtick (`) 3개 사용

  ```python
  print('hello')
  ```

> Inline Code block
- backtick (`) 1개 사용
  
  `마크다운`

---

## 링크

> 문자열 링크

- ([문자열](url)) 사용

  * [구글](https://google.com)
  * [a 파일](a.md)
  * [b  폴더 b.txt](b/b)

> 이미지 링크
- (![이미지파일](1.png))

---

## 인용문
> 인용문

- ( > )사용
  - 정의 할 때 자주 사용

---

## 텍스트 강조
> 볼드체

- (** **)사용
  - **볼드체**

> 기울임체

- (* *)사용
  - *기울임체*

> 라인
- (---)사용

> 줄긋기
- (~~ ~~)사용
  - ~~파이썬~~

---

# CLI

 * Command Line Interface
   - 가상 터미널 또는 텍스트 터미널을 통해 사용자와 컴퓨터가 상호 작용하는 방식
  
> 구성요소
  - 프롬프트 기본 인터페이스
    - 컴퓨터 정보
    - 디렉토리
      -  ~ 의 경우 홈 디렉토리를 의미
   -  $

> 명령어 구조
  - 명령어 기본 구조
    - 특정 프로그램을 어떠한 인자와 함께 호출하도록 명령
    - ex) echo 프로그램을 `hello world`로 호출
  ```
  echo 'hello world'
  hello world
  ```
  ```
  which echo
  /usr/bin/echo
  ```

> 기초 파일시스템 명령어
  - pwd( print working directory )
    - 현재 디렉토리 출력
  - cd 디렉토리 이름 ( change directory)
    - 디렉토리 이동
    - . : 현재 디렉토리
    - .. : 상위 디렉토리
  - ls ( list) 
    - 목록
  - mkdir ( make directory )
    - 디렉토리 생성
  - touch 
    - 파일 생성
  - rm 파일명
    - 파일 삭제하기
  - rm -r 폴더명 
    - 폴더 삭제하기
    -  