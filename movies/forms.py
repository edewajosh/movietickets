from django import forms
from .models import Ticket, Movies, Comments
class UserRegistrationForm(forms.Form):
    username = forms.CharField(required=True, label='Username', max_length=32, widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.CharField(required=True, label='Email', max_length=32,widget=forms.EmailInput(attrs={'class':'form-control'}))
    password = forms.CharField(required=True, label='Password', max_length=32, widget=forms.PasswordInput(attrs={'class':'form-control'}))


class TicketForm(forms.ModelForm):
    movie = forms.ModelChoiceField(queryset=Movies.objects.all(), widget=forms.Select(attrs={'class': 'hidden', 'class' :'form-control'}))
    class Meta:
        model = Ticket
        fields = '__all__'
        labels = {'username' : 'Username  ','phonenumber':'Phone Number ', 'numberofseats' :'Number of seats  ', 'seats' : 'Seats  ',  'movie' : 'Movie  '}
        widgets = {
            'username':forms.TextInput(attrs = {'class':'form-control'}),
            'phonenumber':forms.TextInput(attrs = {'class':'form-control'}),
            'numberofseats':forms.TextInput(attrs = {'class':'form-control', 'type':'number'}),
            'seats':forms.TextInput(attrs = {'class':'form-control'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        exclude = ['movie', 'date_posted']
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'comment':forms.Textarea(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),

        }