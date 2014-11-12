from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Producto(models.Model):
	nombre=models.CharField(max_length=30,null=False)
	descripcion=models.CharField(max_length=500,null=False)
	precio=models.FloatField(null=False)
	stock=models.IntegerField(default=0)

class Pedido(models.Model):
	cliente=models.ForeignKey(User)
	producto=models.ManyToManyField(Producto)
	cantidad=models.IntegerField()
	precio_total=models.FloatField()
	fecha=models.DateTimeField(auto_now_add=True)
	def __unicode__(self):
		return self.producto