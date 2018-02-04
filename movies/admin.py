from django.contrib import admin
from .models import Movies

class MoviesAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_posted', 'showing_at')
admin.site.register(Movies, MoviesAdmin)

