from django.shortcuts import render, redirect
from .models import Adres
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm
import pyodbc

def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Konto zostało założone. Możesz się zarejestrować.')
			return redirect('login')
	else:
		form = UserRegisterForm()
	return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
	if request.method == 'POST':
		u_form = UserUpdateForm(request.POST, instance=request.user)
		if u_form.is_valid():
			conn=pyodbc.connect('Driver={sql server};'
						'Server=localhost;'
						'Database=BankKrwi;'
						'Trusted_Connection=yes;')
			cursor=conn.cursor()
			search = request.user.username
			ulica = request.POST.get('ulica')
			numerMieszkania = request.POST.get('numerMieszkania')
			miasto = request.POST.get('miasto')
			kodPocztowy = request.POST.get('kodPocztowy')
			kraj = request.POST.get('kraj')
			cursor.execute("select * from Adres")
			cursor.execute("update Adres set Ulica = ?, NumerMieszkania = ?, Miasto = ?, KodPocztowy = ?, Kraj = ? from adres as a join dawca as dw on a.AdresID = dw.idAdres where dw.NumerPesel = ?", [ulica, numerMieszkania, miasto, kodPocztowy, kraj, search])
			conn.commit()
			#result = cursor.fetchall()
			#u_form.save()
			messages.success(request, f'Twoje dane adresowe zostały zaktualizowane.')
			return redirect('profile')
	else:
		u_form = UserUpdateForm(instance=request.user)
	context = {
		'u_form': u_form 
	}

	return render(request, 'users/profile.html', context)


@login_required
def adres(request):
	conn=pyodbc.connect('Driver={sql server};'
						'Server=localhost;'
						'Database=BankKrwi;'
						'Trusted_Connection=yes;')
	cursor=conn.cursor()
	search = request.user.username
	cursor.execute("select dw.Imie,dw.Nazwisko,a.Ulica,a.NumerMieszkania,a.Miasto,a.KodPocztowy,a.Kraj from Adres as a join Dawca as dw on dw.idAdres = a.AdresID where dw.NumerPesel = ?", [search])
	result = cursor.fetchall()
	return render(request, 'users/adres.html', {'Adres':result})


