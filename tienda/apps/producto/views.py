from django.shortcuts import render, render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from models import *
from forms import *
import datetime
# Create your views here.

def producto(request):
	if request.method=="POST":
		form=fProducto(request.POST)
		if(form.is_valid()):
			form.save()
	return render_to_response("productos.html",{"Producto":fProducto()},RequestContext(request))

def listar_producto(request,id):
	pro=Producto.objects.all()
	return render_to_response("listar_producto.html",{'Producto':pro},context_instance=RequestContext(request))

def pedido(request,id):
    if request.method=="POST":
		form=fPedido(request.POST)
		if(form.is_valid()):
			form.save()
    return render_to_response("pedido.html",{'Pedido':fPedido},context_instance=RequestContext(request))
