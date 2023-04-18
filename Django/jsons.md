1. python manage.py dumpdata --indent 4 articles.article > articles.json
2. python manage.py dumpdata --indent 4 accounts.user > users.json
3. python manage.py dumpdata --indent 4 articles.comment > comments.json
4. articles / fixtures 폴더 생성
5. 위의 3개를 fixtures에 넣기
6. python manage.py migrate
7. python manage.py loaddata articles.json comments.json users.json