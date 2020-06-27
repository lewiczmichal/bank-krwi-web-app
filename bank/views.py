from django.shortcuts import render
from .models import Sqlserver
from django.contrib.auth.decorators import login_required
import pyodbc


def home(request):
	return render(request, 'bank/home.html')

@login_required
def donacje(request):
	conn=pyodbc.connect('Driver={sql server};'
						'Server=localhost;'
						'Database=BankKrwi;'
						'Trusted_Connection=yes;')
	cursor=conn.cursor()
	search = request.user.username
	cursor.execute("select dw.Imie,dw.Nazwisko,dn.Ilosc,dn.DataDonacji from Dawca as dw join Donacje as dn on dn.idDawca = dw.DawcaID where dw.NumerPesel = ?", [search])
	result = cursor.fetchall()
	return render(request, 'bank/donacje.html', {'Sqlserver':result})

	