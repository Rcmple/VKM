from django.urls import path
from strains.strain_views import change_views
from strains.strain_views import list_views

urlpatterns = [

    # change views
    path('add/', change_views.StrainNewRequestView.as_view(), name='StrainNewRequest'),
    path('add/approve', change_views.StrainNewRequestApproveView.as_view(), name='StrainNewRequestApprove'),
    path('add/reject', change_views.StrainNewRequestRejectView.as_view(), name='StrainNewRequestReject'),
    path("<int:strain_id_param>/edit/", change_views.StrainChangeRequestView.as_view(), name="StrainChangeRequest"),
    path("<int:strain_id_param>/edit/approve", change_views.StrainChangeRequestApproveView.as_view(),
         name="StrainChangeRequestApprove"),
    path("<int:strain_id_param>/edit/reject", change_views.StrainChangeRequestRejectView.as_view(),
         name="StrainChangeRequestReject"),
    path('upload/', change_views.StrainsUploadRequestView.as_view(), name='StrainsUploadRequest'),

    # List views
    path("<int:strain_id_param>/", list_views.StrainInfoView.as_view(), name="StrainInfo"),
    path('get_strains/', list_views.StrainsListView.as_view(), name='StrainsList'),
    path('get_changed_strains/', list_views.StrainChangeRequestListView.as_view(), name='ChangedStrainsList'),
    path('get_my_changed_strains/', list_views.MyStrainChangeRequestListView.as_view(), name='MyChangedStrainsList'),
    path('get_new_strains/', list_views.StrainNewRequestListView.as_view(), name='NewStrainsList'),
    path('get_my_new_strains/', list_views.MyStrainNewRequestListView.as_view(), name='MyNewStrainsList'),
]
