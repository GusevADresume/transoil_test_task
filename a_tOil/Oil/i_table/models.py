from django.db import models


class infotable(models.Model):
    vin = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=5)
    yaer = models.IntegerField()
    maker = models.CharField(max_length=30)
    model = models.CharField(max_length=50)
    e_vehicle_type = models.CharField(max_length=50)
    e_range = models.IntegerField()
    legislative_district = models.IntegerField()
    electric_utility = models.CharField(max_length=100)