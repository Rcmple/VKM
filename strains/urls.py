from django.urls import path
from strains import views
urlpatterns = [
    path('add/', views.StrainNewRequestView.as_view(), name='StrainNewRequest'),
    path("<int:strain_id>/edit/", views.StrainChangeRequestView.as_view(), name="StrainChangeRequest"),
    path('upload/', views.StrainsUploadRequestView.as_view(), name='StrainsUploadRequest'),
    path('get_strains/', views.StrainsListView.as_view(), name='StrainsList'),
    path('get_changed_strains/', views.StrainChangeRequestListView.as_view(), name='ChangedStrainsList'),
    path('get_new_strains/', views.StrainNewRequestListView.as_view(), name='NewStrainsList'),
    path("<int:strain_id>/", views.StrainInfoView.as_view(), name="StrainInfo"),
]
