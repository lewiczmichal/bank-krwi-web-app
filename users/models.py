from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.user.username} Profile'


class Adres(models.Model):
	imie=models.CharField(max_length=50)
	nazwisko=models.CharField(max_length=50)
	ulica = models.CharField(max_length=50)
	numerMieszkania = models.IntegerField()
	miasto = models.CharField(max_length=50)
	kodPocztowy = models.CharField(max_length=50)
	kraj = models.CharField(max_length=50)