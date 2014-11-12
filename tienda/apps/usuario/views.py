from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User,Group
from models import Perfil
from forms import *
# Create your views here.
def portal(request):
    return render_to_response("portal.html",context_instance=RequestContext(request))
def ingresar(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect("/usuario/tipo/")
    else:
        if request.method=='POST':
            formulario=AuthenticationForm(request.POST)
            if formulario.is_valid:
                usuario=request.POST['username']
                contrasena=request.POST['password']
                acceso=authenticate(username=usuario,password=contrasena)
                if acceso is not None:
                    if acceso.is_active:
                        login(request,acceso)
                        return HttpResponseRedirect('/usuario/tipo/')
                    else:
                        login(request,acceso)
                        return HttpResponseRedirect("/usuario/activar/")
                else:
                    return HttpResponseRedirect("/errordatos/")
        else:
            formulario=AuthenticationForm()
        return render_to_response('ingresar.html',{'formulario':formulario},context_instance=RequestContext(request))

def salir(request):
    logout(request)
    return HttpResponseRedirect('/')

def activar_usuario(request):
    usuario=request.user
    if  usuario.is_active:
        return HttpResponseRedirect('/usuario/tipo/')
    else:
        if request.method=='POST':
            formulario=ActivarCuenta(request.POST)
            if formulario.is_valid():
                ci=request.POST['ci']
                telefono=request.POST['telefono']
                usuario=User.objects.get(username=request.user)
                #Activamos la cuenta y guardamos los datos
                usuario.is_active=True
                usuario.save()
                #Guardamos los datos del perfil
                perfil=Perfil.objects.get(user=usuario)
                perfil.ci=ci
                perfil.telefono=telefono
                perfil.save()
                return HttpResponseRedirect('/usuario/tipo/')
        else:
            formulario=ActivarCuenta()
        return render_to_response("activar_cuenta.html",{'formulario':formulario},context_instance=RequestContext(request))

def pefil_usuario(request):
    if request.user.is_authenticated():
        usuario=request.user
        if  usuario.is_active:
            context = {
                'usuario'  : usuario,
                'nombre' : usuario.get_full_name(),
                'perfil' : usuario.get_profile(),
                }
            return render_to_response("usuario_perfil.html",context,context_instance=RequestContext(request))
        else:
            return HttpResponseRedirect("/usuario/activar/")
    else:
        return HttpResponseRedirect("/usuario/ingresar/")


def registro_usuario(request):
    if request.method=='POST':
        formulario=fusuario(request.POST)
        formulario2=fperfil(request.POST)
        if formulario.is_valid() and formulario2.is_valid():
            usuario=request.POST['username']
            formulario.save()
            anio=request.POST['fecha_nacimiento_year']
            mes=request.POST['fecha_nacimiento_month']
            dia=request.POST['fecha_nacimiento_day']
            fecha_nacimiento=anio+"-"+mes+"-"+dia
            sexo=request.POST['sexo']
            #obtenemos el usuario
            nuevo_usuario=User.objects.get(username=usuario)
            perfil=Perfil.objects.create(user=nuevo_usuario,fecha_nacimiento=fecha_nacimiento,sexo=sexo)
            #Seleccionamos el grupo de clientes y si no existe lo creamos
            grupo,crear_grupo=Group.objects.get_or_create(name='Cliente')
            if crear_grupo != None:
                #Como es un usuario normal lo enviamos al grupo de clientes
                nuevo_usuario.groups.add(grupo)
                #Cambiamos algunos atributos como el activo y lo colocamos en falso ya que falta por activar su cuenta
                nuevo_usuario.is_active=False
                nuevo_usuario.is_staff=False
                nuevo_usuario.is_superuser=False
                nuevo_usuario.save()
                return HttpResponseRedirect("/usuario/ingresar/")
            else:
                return HttpResponseRedirect("/error/")
    else:
        formulario=fusuario()
        formulario2=fperfil()
    return render_to_response("registro_usuario.html",{'formulario':formulario,'formulario2':formulario2},context_instance=RequestContext(request))