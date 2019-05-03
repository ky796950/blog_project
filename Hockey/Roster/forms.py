from django import forms
from Roster.models import Post, Comment
 
class PostForm(forms.ModelForm):
    """Form to allow you to enter a blog post."""
 
    class Meta:
        model = Post
        fields = ('author','title','text')
 
        widgets = {
            'title': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.TextInput(attrs={'class': 'editable medium-editor-textarea postcontent'}),
        }
 
class CommentForm(forms.ModelForm):
    """Form to allow you to enter a comment on a post"""
 
    class Meta:
        model = Comment
        fields = ('author','text')
 
        widgets = {
            'author': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.TextInput(attrs={'class': 'editable medium-editor-textarea'}),
        }