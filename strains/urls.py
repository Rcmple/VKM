from django.contrib import admin
from django.urls import path
from django.urls import include
from strains import views
urlpatterns = [
    path('', views.strains, name='strains'),
    path('add/', views.add_strain, name='add_strain'),
]
