from django.conf.urls import patterns, url
from iptonation import views

urlpatterns = patterns('',
            url(r'^$', views.index, name='index'),
            )
