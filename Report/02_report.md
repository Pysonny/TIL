# GIT
> git이란?
- 분산버전관리시스템
- 로컬 버전 관리
---

## Git 사용법
1. 작업한다
2. 변경된 파일 모은다 (add)
3. 버전으로 만든다 (commit)

![flow](../images/git%20flow.jpg)

### 코드

>`Git init`
- 특정 폴더에 git 저장소 만들고 버전 관리

>`git add`
- 작업한 문서들을 1차 정리함에 넣는것

>`git commit -m ' *** '`
- 1차 정리된 파일들을 버전으로 업데이트

>`git status`
- 저장소에 있는 파일 상태 확인

> `git log`
- 저장소에 기록된 커밋 조회
  - `git log -1`
  - `git log --oneline`
  - `git log -2 --oneline`

>`git config -l`
- 내 정보 설정 확인

>`git push`
- 로컬 저장소의 버전을 원격저장소로 보냄
- push가 되지않을 때 방법
  - main / master 확인
  - rejected 될 때
    - `git push origin +master/main`


>`git pull `
- 원격 저장소의 버전을 로컬 저장소로 가져옴

>`git clone`
- 원격 저장소를 복제하여 가져옴

> pull과 clone의 차이점
- clone : 원격저장소 복제
- pull : 원격저장소 커밋가져오기

>`git remote`
  - 원격저장소 사용
    - // -v 
      - 원격저장소 정보 확인
    - // add <원격저장소><url>
      - 원격저장소 추가(origin)
    - // rm <원격저장소>
      - 원격저장소 삭제
> gitignore
  - 파일 무시용 파일
    - 파일
      - *.파일방식
    - 폴더
      - (name)/
  - [주소](https://github.com/github/gitignore)
    