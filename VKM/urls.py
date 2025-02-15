from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views
from VKM.views import csrf_token_view
urlpatterns = [
    path('api/', views.main_page, name='main_page'),
    path('admin', admin.site.urls),
    path('api/strains/', include('strains.urls')),

    path('api/auth/', include('VKMauth.urls')),
    path('api/csrf/', csrf_token_view, name='csrf_token'),
]
