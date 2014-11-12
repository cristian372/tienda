from django import forms
from django.forms import ModelForm
from .models import *
from django.forms.extras.widgets import SelectDateWidget
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class fProducto(ModelForm):
	class Meta:
		model=Producto
class fPedido(ModelForm):
	class Meta:
		model=Pedido