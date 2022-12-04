from django.db import models

# Create your models here.
class Topping(models.Model):
    topping_name=models.CharField(max_length=50)
    topping_amount=models.FloatField()

class Pizza(models.Model):
    toppings=models.ManyToManyField(Topping)
    pizza_name=models.CharField(max_length=50)

