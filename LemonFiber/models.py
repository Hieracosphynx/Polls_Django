import datetime

from django.db import models
from django.utils import timezone
# Create your models here.
class Fruit(models.Model):
    fruit_name = models.CharField(max_length=200)
    def __str__(self):
        return self.fruit_name

class Amount(models.Model):
    amount_fruit = models.IntegerField(default=0)
