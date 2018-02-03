from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    #return HttpResponse("Am not sure why this is not working")
    return render(request, 'movies/index.html')
