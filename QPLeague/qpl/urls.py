from django.conf.urls import url

from . import views

urlpatterns = [
            url(r'^fixtures$', views.fixtures, name='fix'),
            url(r'^player/(?P<name>\w+)/details$', views.details, name='player'),
            url(r'^$', views.index, name='index'),
            url(r'^teams/(?P<name>\w+)$', views.teams, name='teams'),
            ]
