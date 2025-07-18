from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth import logout
from django.utils import timezone
from user.models import CustomUser
from .models import Post, Comment, Like
from .forms import NewBlogForm, NewComment
from django.db.models import Q

from django.core.paginator import Paginator

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
    posts_list = Post.objects.order_by('-published_date')
    p = Paginator(posts_list, 3)
    page = request.GET.get('page')
    posts = p.get_page(page)
    almost_final_page = posts.paginator.num_pages - 1
    return render(request, 'home.html', {'user': user, 'posts': posts, 'almost_final_page': almost_final_page})

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    comment_list = Comment.objects.all().filter(post=post).order_by('-published_date')
    if request.method == 'POST':
        if request.POST.get('like-button') == 'like':
            Like.objects.create(user=request.user, post=post)
        elif request.POST.get('like-button') == 'unlike':
            Like.objects.get(user=request.user, post=post).delete()
        elif request.POST.get('create-comment') == 'comment':
            form = NewComment(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.author = request.user
                comment.post = post
                comment.published_date = timezone.now()
                comment.save()
    c = Paginator(comment_list, 5)
    page = request.GET.get('page')
    comments = c.get_page(page)
    almost_final_page = comments.paginator.num_pages - 1
    liked = post.likers.filter(username=request.user.username).exists()
    likes = post.likers.count()
    form = NewComment()
    return render(request, 'post_detail.html', {'post': post, 'likes': likes, 'liked': liked, 'form': form, 'comments': comments, 'almost_final_page': almost_final_page})

def post_edit(request, pk):
    post = Post.objects.get(pk=pk)
    pub_date = post.published_date
    if request.method== 'POST':
        if request.POST.get('edit-type') == 'edit-blog':
            form = NewBlogForm(request.POST, request.FILES, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.published_date = pub_date
                post.edited_date = timezone.now()
                post.save()
                return redirect('post_detail', pk=pk)
        elif request.POST.get('edit-type') == 'delete-blog':
            Post.objects.filter(pk=pk).delete()
            return redirect('home')
    else:
        form = NewBlogForm(instance=post)
    return render(request, 'post_edit.html', {'form': form})

def search_result(request):
    user=request.user
    search_str = request.GET.get('search-bar')
    posts_list = Post.objects.filter(Q(title__icontains=search_str) | Q(author__username__icontains=search_str)).order_by('-published_date')
    if posts_list is not None:
        p = Paginator(posts_list, 3)
        page = request.GET.get('page')
        posts = p.get_page(page)
        almost_final_page = posts.paginator.num_pages - 1
    else: 
        posts = False
    return render(request, 'search_result.html', {'posts': posts, 'user': user, 'almost_final_page': almost_final_page, 'search_str': search_str})

def likers_view(request, pk):
    post = Post.objects.get(pk=pk)
    likes = Like.objects.filter(post=post)
    liker_info = [(liker.user, liker.date_liked) for liker in likes]
    return render(request, 'likers_view.html', {'post': post, 'liker_info':liker_info})