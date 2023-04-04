from django import forms
from .models import Article
# 1
# class ArticleForm(forms.From):
#     title = forms.CharField(max_length=10)
#     # 위젯 추가
#     content = forms.CharField(widget=forms.Textarea)
    
# 2 modelForm class
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'