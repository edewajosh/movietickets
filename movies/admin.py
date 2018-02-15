from django.contrib import admin
from .models import Movies,Ticket

class MoviesAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_posted', 'showing_at')
admin.site.register(Movies, MoviesAdmin)

class TicketAdmin(admin.ModelAdmin):
    list_display = ('username','movie', 'phonenumber','numberofseats', 'seats')
admin.site.register(Ticket, TicketAdmin)