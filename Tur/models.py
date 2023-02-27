from django.db import models

# Create your models here.
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
        return self.author + ' - ' + self.tour.name