from django.shortcuts import render
from django.http import HttpResponse
from .models import Movies

def index(request):
    movies = Movies.objects.order_by('-date_posted')[:6]
    context = {
        'movies' : movies
    }
    return render(request, 'movies/index.html', context)

def details(request):
    movies = Movies.objects.order_by('-date_posted')
    context = {
        'movies' : movies
    }
    return render(request, 'movies/details.html', context)
