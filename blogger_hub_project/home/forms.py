from django import forms
from .models import Post

class NewBlogForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'post_image']