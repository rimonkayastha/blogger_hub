from django import forms
from .models import Post
from .models import Comment

class NewBlogForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'post_image']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'post-title-input'
            }
            ),
            'text': forms.Textarea(attrs={
                'class': 'post-text-input'
            }),
            'post_image': forms.ClearableFileInput(
                attrs={
                    'class': 'post-file-input'
                }
            ),
        }

class NewComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'comment-input',
                'placeholder': 'Any thoughts?'
            })
        }