from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views
urlpatterns = [
    path('api/', views.main_page, name='main_page'),
    path('admin', admin.site.urls),
    path('api/strains/', include('strains.urls')),

    path('api/auth/', include('VKMauth.urls')),
]
