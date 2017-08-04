from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^index/', index, name='index'),
    url(r'^show/(?P<id>[0-9]+)', show, name='show'),
    url(r'^showAction/(?P<id>[0-9]+)', showAction, name='showAction'),
]