from django.urls import path
from . import views

urlpatterns = [
    path('', views.default_direct, name='default_direct'),
    path('login/', views.login_page, name='login_page'),
    path('signup/', views.signup_page, name='signup_page'),
    path('account/', views.account_page, name='account_page'),
]