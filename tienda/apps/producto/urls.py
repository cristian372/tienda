from django.conf.urls import patterns, url
from views import *
urlpatterns=patterns("",
    url(r'^producto/$',producto),
    url(r'^pedido/$',pedido),
    url(r'^producto/listar/$',listar_producto),
)