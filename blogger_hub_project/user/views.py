from django.shortcuts import render, redirect
from .models import CustomUser
from .forms import UserLoginForm

# Create your views here.
def login_page(request):
    if request.user.is_authenticated:
        return redirect('main_home')
    if request.method == 'POST': 
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            if CustomUser.objects.filter(email=email, password=password).exists():
                return redirect('main_home')
            else:
                messages.error(request, 'Invalid email or password')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})