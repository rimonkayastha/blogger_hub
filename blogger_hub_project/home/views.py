from django.shortcuts import render, HttpResponse

# Create your views here.
def main_home(request):
    return HttpResponse("What's up?")