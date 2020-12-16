from django import forms
from .models import Comment


class SearchForm(forms.Form): 
    word = forms.CharField(label='Search Word')

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=('author_name', 'comment_text')