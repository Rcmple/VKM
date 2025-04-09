from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
urlpatterns = [
    path('api/', views.main_page, name='main_page'),
    path('admin', admin.site.urls),
    path('api/strains/', include('strains.urls')),
    path('api/strains/search/', include('search.urls')),
    path('api/auth/', include('VKMauth.urls')),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path('api/schema/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path("api/docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
]
