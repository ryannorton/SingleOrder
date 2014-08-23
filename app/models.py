from django.db import models
from django.contrib.auth.models import User

class Meal(models.Model):
	group = models.CharField(max_length=30, blank=False, null=False, unique=True)
	# host = models.ForeignKey(User)
	restaurant = models.CharField(max_length=30, blank=False, null=False, unique=False)
	date = models.DateTimeField(auto_now_add=True)
	date.editable=True

class Order(models.Model):
	meal = models.ForeignKey(Meal)
	user = models.ForeignKey(User)

class Item(models.Model):
	order = models.ForeignKey(Order)
	name = models.CharField(max_length=30, blank=False, null=False, unique=False)
	custom = models.CharField(max_length=30, blank=True, null=True, unique=False)
	price = models.DecimalField(max_digits=4, decimal_places=2, null=True)
