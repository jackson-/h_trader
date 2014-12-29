from django.db import models

# Create your models here.
class Stock(models.Model):
	ticker = models.CharField(max_length=5)
	date = models.DateField()
	price = models.IntegerField()

class Portfolio(models.Model):
	balance = models.BigIntegerField()
	initial_balance = models.BigIntegerField(default=10000)

class StocksOwned(models.Model):
	ticker = models.CharField(max_length=5)
	date = models.DateField()
	price = models.IntegerField()
	portfolio = models.ForeignKey(Portfolio)
