from django.db import models



class People(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)


class LocationRecord(models.Model):
    people = models.ForeignKey(People, on_delete=models.CASCADE)
    datetime = models.DateTimeField()
    latitude = models.FloatField()
    longitude = models.FloatField()
