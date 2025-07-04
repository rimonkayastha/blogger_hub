from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import logout

# Create your views here.
def main_home(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    else:
        return redirect('login_page')

def new_blog(request):
    return render(request, 'newblog.html')

def page_redirect(request):
    if request.method == 'POST':
            if request.POST.get('redirect-type') == 'logout':
                logout(request)
                return redirect('login_page')
            if request.POST.get('redirect-type') == 'create-new':
                return redirect('new_blog')
            if request.POST.get('redirect-type') == 'home-direct':
                return redirect('main_home')
            if request.POST.get('redirect-type') == 'account':
                return redirect('account_page')
