#encoding:utf-8
from django.forms import ModelForm
from django.forms.extras.widgets import SelectDateWidget
from django import forms
from models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class ActivarCuenta(forms.Form):
    ci=forms.CharField(widget=forms.TextInput(attrs={'maxlength':8}), required=True)
    telefono=forms.CharField(max_length=7,required=True)

lista_anios = range(2013,1905,-1)
CHOICES = (('1', 'Hombre',), ('2', 'Mujer',))
class fperfil(ModelForm):
    fecha_nacimiento=forms.DateField(initial='dia-mes-anio',widget=SelectDateWidget(years=lista_anios))
    sexo=forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
    class Meta:
        model=Perfil
        exclude = ['user','imagen','ci','telefono']

class fusuario(UserCreationForm):
    username = forms.CharField(max_length=40,required=True,help_text=False,label="Nombre de usuario")
    password2 = forms.CharField(help_text=False,label="Contraseña de confirmacion",widget=forms.PasswordInput)
    first_name=forms.CharField(max_length=40,required=True,label="Nombre")
    last_name=forms.CharField(max_length=50,required=True,label="Apellidos")
    email=forms.EmailField(max_length=60,required=True,label="Email",widget=forms.TextInput)
    class Meta:
        model=User
        fields=("username","password1","password2","first_name","last_name","email")
    def save(self, commit=True):
        user=super(fusuario,self).save(commit=False)
        user.first_name=self.cleaned_data.get("first_name")
        user.last_name=self.cleaned_data.get("last_name")
        user.email=self.cleaned_data.get("email")
        if commit:
            user.save()
        return user