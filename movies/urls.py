from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('details/', views.details, name='details'),
    path('register/', views.register, name='register'),
    path('ticket/', views.ticketView, name='ticketView'),
    path('booked/<int:id>', views.booked, name='booked'),
    path('movie/<int:id>/', views.movie, name='movie'),

]
