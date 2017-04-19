from django.db import models

# Create your models here.

class Logitude_Latitude(models.Model):
    name = models.CharField(max_length=128, blank=True)
    address = models.CharField(max_length=200, blank=True)
    longi = models.DecimalField(max_digits=8, decimal_places=3)
    lat = models.DecimalField(max_digits=8, decimal_places=3)
    radius =models.DecimalField(max_digits=8, decimal_places=3)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Parking(models.Model):
    parking_spot = models.CharField(max_length=128, blank=True)
    time_range = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name


