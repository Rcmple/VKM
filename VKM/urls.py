from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views
urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('admin', admin.site.urls),
    path('strains/', include('strains.urls')),

    path('auth', include('VKMauth.urls')),
]
