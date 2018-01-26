from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.projects, name='projects_all'),
    url(r'^(?P<active_category>.+)/$', views.projects, name='projects_cat'),
    url(r'^(?P<active_year>.+)/$', views.projects, name='projects_year')
]
