from django.db import models

from places.fields import PlacesField


class Place(models.Model):
    location = PlacesField(blank=True)

    def __unicode__(self):
        return self.location.place

    def __str__(self):
        return self.__unicode__()


class Route(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class RoutePoint(models.Model):
    name = models.CharField(max_length=50)
    location = PlacesField()
    route = models.ForeignKey(Route, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
