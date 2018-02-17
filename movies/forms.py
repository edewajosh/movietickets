from django import forms
from .models import Ticket, Movies
class UserRegistrationForm(forms.Form):
    username = forms.CharField(required=True, label='Username', max_length=32)
    email = forms.CharField(required=True, label='Email', max_length=32)
    password = forms.CharField(required=True, label='Password', max_length=32, widget=forms.PasswordInput())


class TicketForm(forms.ModelForm):
    movie = forms.ModelChoiceField(queryset=Movies.objects.all())
    class Meta:
        model = Ticket
        fields = '__all__'
        labels = {'username' : 'Username  ','phonenumber':'Phone Number ', 'numberofseats' :'Number of seats  ', 'seats' : 'Seats  ',  'movie' : 'Movie  '}
