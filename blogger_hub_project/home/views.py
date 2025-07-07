from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth import logout
from django.utils import timezone
from user.models import CustomUser
from .models import Post
from .forms import NewBlogForm

# Create your views here.
def main_home(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        return redirect('login_page')

def new_blog(request):
    if request.method == 'POST':
        form = NewBlogForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit = False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('main_home')
        else:
            return render(request, 'newblog.html', {'form': form})
    else:
        form = NewBlogForm()
        return render(request, 'newblog.html', {'form': form})

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

def home(request):
    user = request.user
    posts = Post.objects.order_by('published_date')
    return render(request, 'home.html', {'user': user, 'posts': posts})

