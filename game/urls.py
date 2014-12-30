from django.conf.urls import patterns, include, url
from django.contrib import admin
from game.views import *

urlpatterns = patterns('',
    # Examples:
    url(r'^round/$', RoundView.as_view(), name='round'),
    url(r'^create/$', CreateView.as_view(), name='create'),
    url(r'^$', StartView.as_view(), name='start'),
)
