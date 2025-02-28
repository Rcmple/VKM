from django.contrib import admin
from django.urls import path
from django.urls import include
from strains import views
urlpatterns = [
    path('add/', views.AddStrainView.as_view(), name='AddStrain'),
    path('upload/', views.UploadStrainsView.as_view(), name = 'UploadStrains'),
    path('list/', views.StrainsListView.as_view(), name = 'StrainsList'),
    path("list/strain/<int:strain_id>/", views.StrainInfoView.as_view(), name="StrainInfo"),
]
