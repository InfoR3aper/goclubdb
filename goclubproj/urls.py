from django.conf.urls import include, url

import goclubdb.views

urlpatterns = [
    url(r'^$', goclubdb.views.index, name='index'),
    url(r'^layers/$', goclubdb.views.layerlist, name='layerlist'),
    url(r'^clubs/(?P<layername>[A-Z]+)', goclubdb.views.clublist, name='clublist'),
    url(r'^club/(?P<clubid>[0-9]+)', goclubdb.views.clubdetail, name='clubdetail'),
]
