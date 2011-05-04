from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('trocaire.encuesta.views',
    (r'^consultar/$', 'consultar'),
    (r'^mujeres-hombres/$', direct_to_template, {'template': 'monitoreo/mujeres-hombres.html'}),
    (r'^mujeres-hombres/(?P<vista>[-\w]+)/$', '_get_view'),
    # (r'^conocimiento/(?P<vista>[-\w]+)/$', '_get_view'),
    
#    (r'^indicadores/$', 'indicadores'),
#    (r'^lista/$', 'lista'),
#    (r'^lista/(?P<id>\d+)/$', 'lista'),
#    (r'^proyecto/(?P<id>\d+)/$', 'proyecto'),
#    (r'^organizacion/(?P<id>\d+)/$', 'organizacion'),
#    (r'^indicadores/(?P<vista>[-\w]+)/$', '_get_view'),
#    (r'^indicadores/meta/(?P<slug>[-\w]+)/$', 'meta'),
)

