from django import forms
from .models import Ticket
class UserRegistrationForm(forms.Form):
    username = forms.CharField(required=True, label='Username', max_length=32)
    email = forms.CharField(required=True, label='Email', max_length=32)
    password = forms.CharField(required=True, label='Password', max_length=32, widget=forms.PasswordInput())


"""class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['username', 'phonenumber', 'numberofseats', 'seats']"""
class TicketForm(forms.Form):
    username = forms.CharField(required=True, label="username", max_length=100)
    phonenumber = forms.CharField(required=True, label="Phone Number", max_length=15)
    numberofseats = forms.IntegerField(required=True, label="Number of Seats")
    seats = forms.CharField(required=True, label="Seats", max_length=30)