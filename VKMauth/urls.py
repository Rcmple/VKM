from django.urls import path
from . import views
urlpatterns = [
    path('login/', views.LoginView.as_view(), name='LoginView'),
    path('logout/', views.LogoutView.as_view(), name='LogoutView'),
    path('status/', views.AuthStatusView.as_view(), name='AuthStatusView'),
]
