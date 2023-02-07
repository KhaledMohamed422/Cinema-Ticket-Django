from django.db import models

# Create your models here.

class Gust(models.Model):
    
    name = models.CharField(max_length=20)
    mobile = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Movie(models.Model):
    
    hall = models.CharField(max_length=20)
    movie = models.CharField(max_length=20)
    date = models.DateField(auto_now_add=True)
        
    def __str__(self):
        return self.movie
    
class Reservation(models.Model):
    
    gust = models.ForeignKey(Gust, related_name="reservation", on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, related_name="reservation", on_delete=models.CASCADE)

