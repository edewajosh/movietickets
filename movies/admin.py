from django.contrib import admin
from .models import Movies,Ticket, Comments

class MoviesInline(admin.TabularInline):
    model = Movies
    extra = 3

class MoviesAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_posted', 'showing_at')
    list_filter = ["date_posted", "showing_at"]
    search_fields = ["name"]
    inline = [MoviesInline]
admin.site.register(Movies, MoviesAdmin)

class TicketAdmin(admin.ModelAdmin):
    list_display = ('username','movie', 'phonenumber','numberofseats', 'seats')
    list_filter = ["movie", "username"]
    search_fields = ["username"]
admin.site.register(Ticket, TicketAdmin)

class CommentsAdmin(admin.ModelAdmin):
    list_display = ('name', 'movie','comment', 'email', 'date_posted')
    list_filter = ['comment']

admin.site.register(Comments, CommentsAdmin)