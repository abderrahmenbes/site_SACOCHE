from unicodedata import name
from django.db import models

# Create your models here.
class Order(models.Model):
    name = models.CharField(max_length=122)
    phone = models .DecimalField(max_digits=11, decimal_places=0)
    adresse = models.CharField(max_length=202)
    prix = models .DecimalField(max_digits=10, decimal_places=2)