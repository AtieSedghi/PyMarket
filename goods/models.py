from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=240)
    price = models.FloatField()
    image_url = models.CharField(max_length=2083)