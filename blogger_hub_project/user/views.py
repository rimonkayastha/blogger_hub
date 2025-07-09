from django.shortcuts import render, redirect, get_object_or_404
from .models import CustomUser
from home.models import Post
from .forms import UserLoginForm
from .forms import UserSignupForm
from .forms import AccountEditForm
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.
def default_direct(request):
    if request.user.is_authenticated:
        return redirect('main_home')
    else:
        return redirect('login_page')

def login_page(request):
    if request.method == 'POST': 
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('main_home')
            messages.error(request, 'Invalid email or password')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})

def signup_page(request):
    if request.method == 'POST': 
        form = UserSignupForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            username = form.cleaned_data['username']
            if CustomUser.objects.filter(email=email).exists():
                messages.error(request, 'User with this email already exists')
            else:
                user = CustomUser.objects.create_user(email=email, password=password, username = username)
                login(request, user)
                return redirect('main_home')
    else:
        form = UserSignupForm()
    return render(request, 'signup.html', {'form': form})

def account_page(request, username):
    Users = CustomUser.objects
    user = get_object_or_404(CustomUser, username=username)
    posts = Post.objects.filter(author=user).order_by('published_date')
    return render(request, 'account.html', {'user': user, 'Users' : Users, 'posts': posts})

def account_edit_page(request, username):
    user = get_object_or_404(CustomUser, username=username)
    if request.method == 'POST':
        form = AccountEditForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect('account_page', username=user.username)
        else:
           return render(request, 'account_edit.html', {'user': user, 'form':form}) 
    else:
        form = AccountEditForm(instance=user)
        return render(request, 'account_edit.html', {'user': user, 'form':form})
