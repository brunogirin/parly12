from django.conf.urls import patterns, url

from rainyday import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^install/$', views.install, name='install'),
    url(r'^install_start/$', views.install_start, name='install_start'),
    url(r'^install_status/$', views.install_status, name='install_status'),
    url(r'^chart_rain/$', views.chart_rain, name='chart_rain'),
    url(r'^chart_dow/$', views.chart_dow, name='chart_dow')
)

