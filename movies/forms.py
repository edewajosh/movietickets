from django import forms
from .models import Ticket, Movies
class UserRegistrationForm(forms.Form):
    username = forms.CharField(required=True, label='Username', max_length=32)
    email = forms.CharField(required=True, label='Email', max_length=32)
    password = forms.CharField(required=True, label='Password', max_length=32, widget=forms.PasswordInput())


class TicketForm(forms.ModelForm):
    movie = forms.ModelMultipleChoiceField(queryset=Movies.objects.all())
    class Meta:
        model = Ticket
        fields = ['username', 'phonenumber', 'numberofseats', 'seats', 'movie',]
        labels = {'username' : 'Username  ', 'phonenumber':'Phone Number ', 'numberofseats' :'Number of seats  ', 'seats' : 'Seats  ', 'movie' : 'Movie  ', }

"""class TicketForm(forms.Form):
    username = forms.CharField(required=True, label="username", max_length=100)
    phonenumber = forms.CharField(required=True, label="Phone Number", max_length=15)
    numberofseats = forms.IntegerField(required=True, label="Number of Seats")
    seats = forms.CharField(required=True, label="Seats", max_length=30)

    movie = forms.ModelMultipleChoiceField(queryset=Movies.objects.all())"""