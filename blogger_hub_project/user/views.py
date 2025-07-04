from django.shortcuts import render, redirect
from .models import CustomUser
from .forms import UserLoginForm
from .forms import UserSignupForm
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
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('main_home')
        else:
            messages.error(request, 'Invalid email or password')
            return render(request, 'login.html', {'form': form})
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

def account_page(request):
    user = request.user
    return render(request, 'account.html', {'user': user})
