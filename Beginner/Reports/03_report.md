# Branch
> Branch란?
- 독립적인 작업흐름 만들고 관리

## 주요 명령어

> 브랜치 생성

``` git branch <b_name >```

> 브랜치 이동

``` git checkout <b_name >```

> 브랜치 생성 및 이동

``` git check out -b <b_name >```

> 브랜치 목록

``` git branch ```

> 브랜치 삭제

``` git branch -d <b_name >```

> 브랜치 합치기

``` git merge <b_name > ```

- 로컬에서 브랜치 삭제하기 명령어 

```git branch -d < b_name > ```

- 원격에서 브랜치 삭제하기 명령어

```git push origin --delete < b_name >```

## Git flow
> Shared Repository Model
- 팀원 초대


> 기본적인 흐름

```
Git init -> touch <file> -> git add . -> git commit -m ‘ name ‘ -> 
git log -> git branch <b_name> - > git checkout <b_name> -> 
touch <file> -> git add. -> git commit -m ‘ name ‘ -> 
git checkout master -> git log –oneline -> git merge <b_name> -> 
git branch -d <b_name>
```

# Folk

- [내용 정리](https://hg-edu.notion.site/GitHub-Pull-Request-fdea6eb3d7054b36ae8ee2888b6e1f9b)