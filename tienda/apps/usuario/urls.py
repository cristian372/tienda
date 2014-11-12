from django.conf.urls import patterns,url
from views import ingresar, registro_usuario
from views import *
urlpatterns=patterns("",
	url(r'^$',portal),
    url(r'^usuario/registro/$',registro_usuario),
    url(r'^usuario/ingresar/$',ingresar),
    url(r'^usuario/salir/$',salir),
    url(r'^usuario/perfil/$',pefil_usuario),
    url(r'^usuario/activar/$',activar_usuario),
)