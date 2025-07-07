from django.urls import path
from . import views

urlpatterns = [
    path('homeredirect/', views.main_home, name='main_home'),
    path('new/', views.new_blog, name='new_blog'),
    path('redirect/', views.page_redirect, name="page_redirect"),
    path('home/', views.home, name='home'),
    path('post/<int:pk>', views.post_detail, name='post_detail'),
    path('post/<int:pk>/edit', views.post_edit, name='post_edit'),
]