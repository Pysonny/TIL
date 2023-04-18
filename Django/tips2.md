## comment

articles/models.py
```py
class Comment(models.Model):
    # 외래 키 필드
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

```
` python manage.py makemigration `
` python manage.py migration `


articles/forms.py
```py
from .models import Article, Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)

```

articles/urls.py
```py
    path('<int:article_pk>/comments/', views.comment_create, name='comment_create'),
    path('<int:article_pk>/comments/<int:comment_pk>/delete/', views.comment_delete, name='comment_delete'),

```


articles/views.py
```py
from .models import Article, Comment
from .forms import ArticleForm, CommentForm

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm()
    # 해당 게시글에 작성된 모든 댓글을 조회(역참조)
    comments = article.comment_set.all()
    context = {
        'article': article,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'articles/detail.html', context)


def comment_create(request, article_pk):
    # 몇 번 게시글인지 조회
    article = Article.objects.get(pk=article_pk)
    # 댓글 데이터를 받아서
    comment_form = CommentForm(request.POST)
    # 유효성 검증
    if comment_form.is_valid():
        # commit을 False로 지정하면 인스턴스는 반환하면서도 DB에 레코드는 작성하지 않도록 함
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.save()
        return redirect('articles:detail', article.pk)
    context = {
        'article': article,
        'comment_form': comment_form,
    }
    return render(request, 'articles/detail.html', context)


def comment_delete(request, article_pk, comment_pk):
    # 삭제할 댓글을 조회
    comment = Comment.objects.get(pk=comment_pk)
    # article_pk = comment.article.pk
    # 댓글 삭제
    comment.delete()
    return redirect('articles:detail', article_pk)
```

articles/detail.html
```html
<h4>댓글 목록</h4>
  <ul>
    {% for comment in comments %}
      <li>
        {{ comment.content }}
        <form action="{% url 'articles:comment_delete' article.pk comment.pk %}" method="POST">
          {% csrf_token %}
          <input type="submit" value="삭제">
        </form>
      </li>
    {% endfor %}
  </ul>
    <hr>
  <form action="{% url 'articles:comment_create' article.pk %}" method="POST">
    {% csrf_token %}
    {{ comment_form }}
    <input type="submit">
  </form>
```


# User
articles/models.py
```py
# models.py에서 User를 참조할때만 다음과 같이 참조한다.
from django.conf import settings


class Article(models.Model):
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  # settings에 AUTH_USER_MODEL = 'accounts.User' 넣고 사용하기 !
  # 일대일 관계에는 단수 (user) / 다대일 관계에는 복수 (users) 사용
```

terminal

` python manage.py makemigrations `
<!-- 한번에 안만들어짐 -->
` 1 `
<!-- 기존 유저들을 1번 으로 하겠다~ -->
` 1 `

` python manage.py migrate `


articles/forms.py
```py
class ArticleForm(forms.ModelForm):
  class Meta:
    model = Article
    fields = ('title', 'content',)
```


articles/views.py
```py
def create(request):
  if request.method == 'POST':
    form = ArticleForm(request.POST)
    if form.is_valid():
      article = form.save(commit=False)
      article.user = request.user
      article.save()
      return redirect('articles:detail', article.pk)
  else:
    form = ArticleForm()
  context = {
    'form': form,
  }
  return render(request, 'articles/create.html', context)
```


articles/detail.html
```html
{% for article in articles %}
  <p>작성자: {{ article.user }}</p>
  <p>제목: 
    <a href="{% url 'articles:detail' article.pk %}">{{ article.title }}</a>
  </p>
  <p>내용: {{ article.content }}</p>
  <hr>
{% endfor %}
```

<!-- 다른 유저의 수정을 금지시키기! -->
articles/views.py
```py
def update(request, article_pk):
  article = Article.objects.get(pk=article_pk)
  # 수정을 요청하는 자 vs 게시글의 작성자 비교
  if request.user == article.user:
    if request.method == 'POST':
      form = ArticleForm(request.POST, instance=article)
      if form.is_valid():
        form.save()
        return redirect('articles:detail', article.pk)
    else:
      form = ArticleForm(instance=article)
  else:
    return redirect('articles:index')
  context = {
    'article': article,
    'form': form,
  }
  return render(request, 'articles/update.html', context)
```

articles/detail.html
```html
{% if request.user == article.user %}
  <form action="{% url 'articles:delete' article.pk  %}" method="POST">
    {% csrf_token %}
    <input type="submit" value="삭제">
  </form>
  <a href="{% url 'articles:update' article.pk %}">[UPDATE]</a>
{% endif %}

```

articles/views.py
```py
def delete(request, article_pk):
  article = Article.objects.get(pk=article_pk)
  if request.user == article.user:
    article.delete()
  return redirect('articles:index')
```


articles/models.py
```py
class Comment(models.Model):
  # 외래 키 필드
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
```


articles/views.py
```py
def comment_create(request, article_pk):
  # 몇 번 게시글인지 조회
  article = Article.objects.get(pk=article_pk)
  # 댓글 데이터를 받아서
  comment_form = CommentForm(request.POST)
  # 유효성 검증
  if comment_form.is_valid():
    # commit을 False로 지정하면 인스턴스는 반환하면서도 DB에 레코드는 작성하지 않도록 함
    comment = comment_form.save(commit=False)
    comment.article = article
    comment.user = request.user
    comment.save()
    return redirect('articles:detail', article.pk)
  context = {
    'article': article,
    'comment_form': comment_form,
  }
  return render(request, 'articles/detail.html', context)

```


articles/detail.html
```html
<!-- 유저 확인 -->
  {{ comment.user }} - {{ comment.content }}
  <!-- 유저여야 삭제 -->
  {% if request.user == comment.user %}
    <form action="{% url 'articles:comment_delete' article.pk comment.pk %}" method="POST">
      {% csrf_token %}
      <input type="submit" value="삭제">
    </form>
  {% endif %}
```


articles/views.py
```py
def comment_delete(request, article_pk, comment_pk):
  # 삭제할 댓글을 조회
  comment = Comment.objects.get(pk=comment_pk)
  # article_pk = comment.article.pk
  
  # 댓글 삭제를 요청하는 자 vs 댓글 작성자
  if request.user == comment.user:
    # 댓글 삭제
    comment.delete()
  return redirect('articles:detail', article_pk)
```