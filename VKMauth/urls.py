from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView
urlpatterns = [
    path('login/', views.LoginView.as_view(), name='LoginView'),
    path('logout/', views.LogoutView.as_view(), name='LogoutView'),
    path('status/', views.AuthStatusView.as_view(), name='AuthStatusView'),

    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
