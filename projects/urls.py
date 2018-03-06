from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.projects, name='projects_all'),
    url(r'^(?P<active_filter>.+)/$', views.projects, name='projects_filtered')
]
