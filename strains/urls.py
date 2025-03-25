from django.urls import path
from strains import views
urlpatterns = [
    path('add/', views.AddStrainView.as_view(), name='AddStrain'),
    path('upload/', views.UploadStrainsView.as_view(), name = 'UploadStrains'),
    path('list/', views.StrainsListView.as_view(), name = 'StrainsList'),
    path('edited_list/', views.EditedStrainsListView.as_view(), name ='SuggestionsList'),
    path("<int:strain_id>/", views.StrainView.as_view(), name="StrainInfo"),
    path("<int:strain_id>/edit/", views.EditedStrainView.as_view(), name="EditStrain"),

]
