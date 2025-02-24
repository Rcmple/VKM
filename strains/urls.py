from django.contrib import admin
from django.urls import path
from django.urls import include
from strains import views
urlpatterns = [
    path('add/', views.AddStrain.as_view(), name='AddStrain'),
    path('upload/', views.UploadStrains.as_view(), name = 'UploadStrains'),
    path('list/', views.ListStrains.as_view(), name = 'ListStrains'),
]
