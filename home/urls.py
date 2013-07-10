from django.conf.urls.defaults import patterns,url
from views import *


urlpatterns = patterns('infosoft.home.views',
             url(r'^$', index,name='vista_principal'),
             url(r'^contacto/$', contacto,name='vista_contacto'),
    )