from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Movies, Comments
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import UserRegistrationForm, TicketForm, CommentForm

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
                messages.success(request, "Account Has been Created Successfully")
                return HttpResponseRedirect('/')
            else:
                raise forms.ValidationError('Looks like a username with that email or password already exist')
    else:
        form = UserRegistrationForm()
    return render(request, 'movies/register.html', {'form' : form})

def ticketView(request):
    form = TicketForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Thank You, You have successfully Reserved the Seat")
        return HttpResponseRedirect('/booked')
    context = {'form': form}  
    return render(request, 'movies/ticket.html',context)

def booked(request,id):
    return render(request, 'movies/ticket_details.html')

def movie(request, id):
    form = CommentForm(request.POST or None)
    movies = get_object_or_404(Movies, pk=id)
    texts = Comments.objects.filter(comment__exact=movies.name)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/movie')
    context = {
        'form':form,
        'movies':movies,
        'texts':texts,
        }
    return render(request, 'movies/movie_details.html', context)