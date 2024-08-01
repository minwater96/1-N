from django import forms
from .models import Article, Comment

class ArticleForm(forms.ModelForm):
    class Meta():
        model = Article
        fields = '__all__'

class CommentForm(forms.ModelForm):
    class Meta():
        model = Comment

        #fields => 추가할 필드 이름 목록 10개중 1개 받을때
        fields = ('content', )

        # exclude => 제거할 필드 이름 목록 10개중 9기
        # fields = ('content', )