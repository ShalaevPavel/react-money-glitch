from django.db import models
from django.contrib import admin
from django.views.generic import ListView, DetailView
from django_admin_geomap import GeoItem


class Marks(models.Model):
    subject_name = models.CharField(max_length=69)
    points = models.ImageField()

    def __str__(self):
        return self.subject_name
    def __str__(self):
        return self.points

class Location(models.Model):
    name = models.CharField(max_length=100)
    lon = models.FloatField()  # долгота
    lat = models.FloatField()

class Location(models.Model, GeoItem):

    @property
    def geomap_longitude(self):
        return str(self.lon)

    @property
    def geomap_latitude(self):
        return str(self.lat)