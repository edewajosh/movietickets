from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .models import Movies
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from .forms import UserRegistrationForm, TicketForm

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
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            username = userObj['username']
            email = userObj['email']
            password = userObj['password']

            if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
                User.objects.create_user(username, email, password)
                user = authenticate(username=username, password=password)
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                raise forms.ValidationError('Looks like a username with that email or password already exist')
    else:
        form = UserRegistrationForm()
    return render(request, 'movies/register.html', {'form' : form})

def ticketView(request):
    form_class = TicketForm
    form = form_class(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            ticket = form.save(commit=True)
            ticket.save()
            return HttpResponseRedirect('/')
        
    return render(request, 'movies/ticket.html', {'form': form})
