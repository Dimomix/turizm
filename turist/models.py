from django.db import models
from turizm.settings import AUTH_PASSWORD_VALIDATORS
from django.utils.translation import gettext_lazy as _

#####################
from django.contrib.auth.models import User
# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100)
    userfname = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    login= models.CharField(max_length=100)
    ID= models.CharField(max_length=100)
    address= models.CharField(max_length=100)
class Employees(models.Model):
    emp_name= models.CharField(max_length=100)
    emp_fname= models.CharField(max_length=100)
    login= models.CharField(max_length=100)
    password= models.CharField(max_length=100)
    job= models.CharField(max_length=100)
    ID= models.CharField(max_length=100)
    
class Country(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=3)

class City(models.Model):
    name = models.CharField(max_length=255)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='cities')
class Way(models.Model):
    TRANSPORT_CHOICES = [
        ('car', _('Car')),
        ('bus', _('Bus')),
        ('train', _('Train')),
        ('plane', _('Plane')),
        ('ship', _('Ship')),
    ]
    transport = models.CharField(max_length=5, choices=TRANSPORT_CHOICES)
    departure_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='departures')
    arrival_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='arrivals')
    duration = models.DurationField()

class Hotel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='hotels')
    address = models.CharField(max_length=200)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    room_type = models.CharField(max_length=50)
    available_rooms = models.IntegerField()
    price = models.FloatField()

class Place(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='places')
    address = models.CharField(max_length=200)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

class Tour(models.Model):
    name = models.CharField(max_length=100)
    destination = models.ForeignKey(City, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    transportation = models.ForeignKey(Way, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    places = models.ManyToManyField(Place, related_name='tours')

class Comment(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    text = models.TextField() 

''' class Hotel(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    room_type = models.CharField(max_length=50)
    available_rooms = models.IntegerField()
    price = models.FloatField()
    description = models.TextField()
 '''

''' 
class Country(models.Model):
    name = models.CharField(max_length=100)
    population = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    population = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Hotel(models.Model):
    name = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.FloatField()

    def __str__(self):
        return self.name


class TouristAgency(models.Model):
    name = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    rating = models.FloatField()

    def __str__(self):
        return self.name


class TouristAttraction(models.Model):
    name = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.FloatField()

    def __str__(self):
        return self.name


class Transportation(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Tour(models.Model):
    name = models.CharField(max_length=100)
    tourist_agency = models.ForeignKey(TouristAgency, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.DurationField()
    hotels = models.ManyToManyField(Hotel)
    tourist_attractions = models.ManyToManyField(TouristAttraction)
    transportation = models.ForeignKey(Transportation, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Comment(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    text = models.TextField()

    def __str__(self):
        return self.author + ' - ' + self.tour.name'''