from django.conf.urls import patterns, url
from units.views import *

urlpatterns = patterns('',
    url(r'^save/$', save),
    url(r'^save/unit(?P<num>[0-9]+)/$', save),
    url(r'^unit(?P<num>[0-9]+)/$', page),
)

