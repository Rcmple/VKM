from django.urls import path
from strains import views
urlpatterns = [
    path('add/', views.StrainNewRequestView.as_view(), name='StrainNewRequest'),
    path("<int:strain_id>/edit/", views.StrainChangeRequestView.as_view(), name="StrainChangeRequest"),
    path('upload/', views.StrainsUploadRequestView.as_view(), name = 'StrainsUploadRequest'),
    path('get_strains/', views.StrainsListView.as_view(), name = 'StrainsList'),
    path("<int:strain_id>/", views.StrainInfoView.as_view(), name="StrainInfo"),
    path("<int:strain_id>/edit/approve", views.StrainChangeRequestView.as_view(), name="StrainChangeRequestApprove"),
]
