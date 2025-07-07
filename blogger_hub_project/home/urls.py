from django.urls import path
from . import views

urlpatterns = [
    path('homeredirect/', views.main_home, name='main_home'),
    path('new/', views.new_blog, name='new_blog'),
    path('redirect/', views.page_redirect, name="page_redirect"),
    path('home/', views.home, name='home'),
]