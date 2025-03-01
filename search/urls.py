from django.urls import path
from . import views

urlpatterns = [
    path('', views.StrainsSearchView.as_view(), name='StrainsSearch'),
]