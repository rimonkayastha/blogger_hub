from django.shortcuts import render, redirect
from .models import CustomUser

# Create your views here.
def login_page(request):
    if request.user.is_authenticated:
        return redirect('main_home')
    return render(request, 'templates/login.html', {})