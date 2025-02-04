from rest_framework import serializers
from .models import Strains
class StrainsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Strains
        fields = '__all__'