from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Movies

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

def index(request):
    movies = Movies.objects.order_by('-date_posted')[:6]
    slides = Movies.objects.order_by('-date_posted')[:4]
    context = {
        'movies' : movies,
        'slides' : slides,
    }
    return render(request, 'movies/index.html', context)

def details(request):
    movies = Movies.objects.order_by('-date_posted')
    context = {
        'movies' : movies
    }
    return render(request, 'movies/details.html', context)

"""
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'movies/signup.html', {'form' : form})
"""