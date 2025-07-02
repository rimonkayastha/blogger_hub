from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import logout

# Create your views here.
def main_home(request):
    if request.method == 'POST':
        if request.POST.get('form-type') == 'logout':
            logout(request)
            return redirect('login_page')
    return render(request, 'home.html')