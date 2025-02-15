from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views
urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('status/', views.auth_status_view, name='auth_status'),
]
