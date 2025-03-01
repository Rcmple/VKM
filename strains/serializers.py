from rest_framework import serializers
from .models import StrainModel, StrainModelChange
class AddStrainSerializer(serializers.ModelSerializer):
    class Meta:
        model = StrainModel
        fields = '__all__'

class PreviewStrainsSerializer(serializers.ModelSerializer):

    class Meta:
        model = StrainModel
        fields = ['strain_id','Genus', 'Species', 'Family', 'Class', 'Risk_group']

class StrainSerializer(serializers.ModelSerializer):
    Type = serializers.SerializerMethodField()
    ReceivedFrom = serializers.SerializerMethodField()
    Depositor = serializers.SerializerMethodField()
    TypeofSubstrate = serializers.SerializerMethodField()
    IsolatedFrom = serializers.SerializerMethodField()
    AnatomicPart = serializers.SerializerMethodField()
    Location = serializers.SerializerMethodField()
    Geographics = serializers.SerializerMethodField()
    Country = serializers.SerializerMethodField()
    CollectedBy = serializers.SerializerMethodField()
    IsolatedBy = serializers.SerializerMethodField()
    IsolatedNumber = serializers.SerializerMethodField()
    IdentificateBy = serializers.SerializerMethodField()
    GrowthCondition = serializers.SerializerMethodField()
    Other = serializers.SerializerMethodField()
    Reidentif = serializers.SerializerMethodField()
    Application = serializers.SerializerMethodField()
    MeraboliteProduction = serializers.SerializerMethodField()
    Transformation = serializers.SerializerMethodField()
    Degradation = serializers.SerializerMethodField()
    EnzymeProduction = serializers.SerializerMethodField()
    class Meta:
        model = StrainModel
        exclude = [
            'TypeRus', 'TypeEng', 'ReceivedFromRus', 'ReceivedFromEng', 'DepositorRus', 'DepositorEng',
            'TypeOfSubstrateRus', 'TypeOfSubstrateEng', 'IsolatedFromRus', 'IsolatedFromEng', 'AnatomicPartRus',
            'AnatomicPartEng', 'LocationRus', 'LocationEng', 'GeographicsRus', 'GeographicsEng', 'CountryRus',
            'CountryEng', 'CollectedByRus', 'CollectedByEng', 'IsolatedByRus', 'IsolatedByEng', 'IsolateNumberRus',
            'IsolateNumberEng', 'IdentificateByRus', 'IdentificateByEng', 'GrowthConditionRus', 'GrowthConditionEng',
            'OtherRus', 'OtherEng', 'ReidentifRus', 'ReidentifEng', 'ApplicationRus', 'ApplicationEng',
            'MeraboliteProductionRus', 'MeraboliteProductionEng', 'TransformationRus', 'TransformationEng',
            'DegradationRus', 'DegradationEng', 'EnzymeProductionRus', 'EnzymeProductionEng'
        ]

    def get_Type(self, obj):
        return {
            'en': obj.TypeEng,
            'ru': obj.TypeRus
        }

    def get_ReceivedFrom(self, obj):
        return {
            'en': obj.ReceivedFromEng,
            'ru': obj.ReceivedFromRus
        }

    def get_Depositor(self, obj):
        return {
            'en': obj.DepositorEng,
            'ru': obj.DepositorRus
        }

    def get_TypeofSubstrate(self, obj):
        return {
            'en': obj.TypeOfSubstrateEng,
            'ru': obj.TypeOfSubstrateRus
        }

    def get_IsolatedFrom(self, obj):
        return {
            'en': obj.IsolatedFromEng,
            'ru': obj.IsolatedFromRus
        }

    def get_AnatomicPart(self, obj):
        return {
            'en': obj.AnatomicPartEng,
            'ru': obj.AnatomicPartRus
        }

    def get_Location(self, obj):
        return {
            'en': obj.LocationEng,
            'ru': obj.LocationRus
        }

    def get_Geographics(self, obj):
        return {
            'en': obj.GeographicsEng,
            'ru': obj.GeographicsRus
        }

    def get_Country(self, obj):
        return {
            'en': obj.CountryEng,
            'ru': obj.CountryRus
        }

    def get_CollectedBy(self, obj):
        return {
            'en': obj.CollectedByEng,
            'ru': obj.CollectedByRus
        }

    def get_IsolatedBy(self, obj):
        return {
            'en': obj.IsolatedByEng,
            'ru': obj.IsolatedByRus
        }

    def get_IsolatedNumber(self, obj):
        return {
            'en': obj.IsolateNumberEng,
            'ru': obj.IsolateNumberRus
        }

    def get_IdentificateBy(self, obj):
        return {
            'en': obj.IdentificateByEng,
            'ru': obj.IdentificateByRus
        }

    def get_GrowthCondition(self, obj):
        return {
            'en': obj.GrowthConditionEng,
            'ru': obj.GrowthConditionRus
        }

    def get_Other(self, obj):
        return {
            'en': obj.OtherEng,
            'ru': obj.OtherRus
        }

    def get_Reidentif(self, obj):
        return {
            'en': obj.ReidentifEng,
            'ru': obj.ReidentifRus
        }

    def get_Application(self, obj):
        return {
            'en': obj.ApplicationEng,
            'ru': obj.ApplicationRus
        }

    def get_MeraboliteProduction(self, obj):
        return {
            'en': obj.MeraboliteProductionEng,
            'ru': obj.MeraboliteProductionRus
        }

    def get_Transformation(self, obj):
        return {
            'en': obj.TransformationEng,
            'ru': obj.TransformationRus
        }

    def get_Degradation(self, obj):
        return {
            'en': obj.DegradationEng,
            'ru': obj.DegradationRus
        }

    def get_EnzymeProduction(self, obj):
        return {
            'en': obj.EnzymeProductionEng,
            'ru': obj.EnzymeProductionRus
        }