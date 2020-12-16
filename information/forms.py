from django import forms
from .models import Comment

class PostSearchForm(forms.Form):
    search_word = forms.CharField(label='Search Word')

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=('author_name', 'comment_text')