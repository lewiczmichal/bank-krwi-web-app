from django.db import models
from django.contrib.auth.models import User

class Sqlserver(models.Model):
	imie=models.CharField(max_length=50)
	nazwisko=models.CharField(max_length=50)
	ilosc=models.DecimalField(max_digits=5, decimal_places=2)
	data=models.DateTimeField()