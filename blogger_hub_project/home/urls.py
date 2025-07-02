from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.main_home, name='main_home'),
]