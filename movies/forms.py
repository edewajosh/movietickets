from django import forms
from .models import Ticket
class UserRegistrationForm(forms.Form):
    username = forms.CharField(required=True, label='Username', max_length=32)
    email = forms.CharField(required=True, label='Email', max_length=32)
    password = forms.CharField(required=True, label='Password', max_length=32, widget=forms.PasswordInput())

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['username', 'phonenumber', 'numberofseats', 'seats']