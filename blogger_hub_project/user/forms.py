from django import forms
from .models import CustomUser

class UserLoginForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'password']

class UserSignupForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'password']