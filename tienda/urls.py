from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tienda.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('tienda.apps.producto.urls')),
    url(r'^', include('tienda.apps.usuario.urls')),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
    {'document_root':settings.MEDIA_ROOT,}),	
)
