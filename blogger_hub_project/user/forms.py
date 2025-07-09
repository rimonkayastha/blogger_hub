from django import forms
from .models import CustomUser

class UserLoginForm(forms.Form):
    email    = forms.EmailField(widget=forms.TextInput(attrs={
        'class': 'email-input',
        'placeholder': 'Email'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'password-input',
        'placeholder': 'Password'
    }), strip=False)

class UserSignupForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'username-input',
                'placeholder': 'Username'
            }),
            'email': forms.TextInput(attrs={
                'class': 'email-input',
                'placeholder': 'Email'
            }),
            'password': forms.PasswordInput(attrs={
                'class': 'password-input',
                'placeholder': 'Password'
            })
        }

class AccountEditForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'profile_image']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'account_input'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'account_input'
            }),
            'username': forms.TextInput(attrs={
                'class': 'account_input'
            }),
            'profile_image': forms.ClearableFileInput(attrs={
                'class': 'account_file_input',
            })
        }