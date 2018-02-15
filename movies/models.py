from django.db import models
from datetime import datetime

class Movies(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField()
    description = models.TextField()
    date_posted = models.DateTimeField(default=datetime.now,blank=True)
    showing_at = models.DateTimeField('Time and Date movie will be showing')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Movies"

class Ticket(models.Model):
    username = models.CharField(max_length=100)
    phonenumber = models.CharField(max_length=15)
    numberofseats = models.IntegerField()
    seats = models.CharField(max_length=30)
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE)

    def __str__(self):
        return self.username

