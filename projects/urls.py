from django.urls import path

from . import views

urlpatterns = [
    path('', views.projects, name='projects_all'),
    path('<str:cat_filter>/', views.projects, name='projects_filtered')
]
