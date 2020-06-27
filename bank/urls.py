from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='bank-home'),
    path('donacje/', views.donacje, name='bank-donacje'),
]
