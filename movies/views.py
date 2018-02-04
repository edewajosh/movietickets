from django.shortcuts import render
from django.http import HttpResponse
from .models import Movies

def index(request):
    movie = Movies.objects.order_by('-date_posted')
    context = {
        'movie' : movie
    }
    return render(request, 'movies/index.html', context)
