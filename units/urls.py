from django.conf.urls import patterns, url
from units.views import *

urlpatterns = patterns('',
    url(r'^save/$', save, name="save"),
    url(r'^save/unit(?P<num>[0-9]+)/$', save, name="save_unit"),
    url(r'^unit(?P<num>[0-9]+)/$', page, name="page"),
    url(r'^mylist/$', mylist, name="mylist"),
)

