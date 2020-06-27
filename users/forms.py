from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
	#email = forms.EmailField()
	username = forms.CharField(label = "Pesel")

	class Meta:
		model = User
		fields = ['username', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
	ulica = forms.CharField(label = "Ulica")
	numerMieszkania = forms.IntegerField(label = "Numer Mieszkania")
	miasto = forms.CharField(label = "Miasto")
	kodPocztowy = forms.CharField(label = "Kod Pocztowy")
	kraj = forms.CharField(label = "Kraj")

	class Meta:
		model = User
		fields = ['ulica', 'numerMieszkania', 'miasto', 'kodPocztowy', 'kraj'] 
