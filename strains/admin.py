from django.contrib import admin

from strains.models import StrainModel, StrainNewRequestModel, StrainChangeRequestModel

# Register your models here.

admin.site.register(StrainModel)
admin.site.register(StrainNewRequestModel)
admin.site.register(StrainChangeRequestModel)