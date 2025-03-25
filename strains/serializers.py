from rest_framework import serializers
from .models import StrainModel, StrainChangeModel
from VKMauth.serializers import UserSerializer

class Section1Serializer(serializers.ModelSerializer):
    Type = serializers.SerializerMethodField()

    class Meta:
        model = StrainModel
        fields = [
            'CollectionCode', 'Subcollection', 'Subcollection1', 'Genus', 'Species', 'Variant',
            'Forma', 'FormaSpecies', 'Strain', 'AuthoritySp', 'AuthoritySubSp', 'Family',
            'Order', 'Class', 'Synonym', 'TaxonomicID', 'Current_Name', 'Link_to_TaxonomicID',
            'Pathogenicgroup', 'Risk_group', 'SanPin', 'State', 'Type', 'Qouts',
            'OtherName', 'ClassShort', 'References', 'References_nc', 'Race', 'Serovar', 'OtherCol'
        ]

    def get_Type(self, obj):
        return {
            'en': obj.TypeEng,
            'ru': obj.TypeRus
        }


class Section2Serializer(serializers.ModelSerializer):
    ReceivedFrom = serializers.SerializerMethodField()
    Depositor = serializers.SerializerMethodField()
    TypeOfSubstrate = serializers.SerializerMethodField()
    IsolatedFrom = serializers.SerializerMethodField()
    AnatomicPart = serializers.SerializerMethodField()
    Location = serializers.SerializerMethodField()
    Geographics = serializers.SerializerMethodField()
    Country = serializers.SerializerMethodField()
    CollectedBy = serializers.SerializerMethodField()
    IsolatedBy = serializers.SerializerMethodField()
    IsolateNumber = serializers.SerializerMethodField()
    IdentificateBy = serializers.SerializerMethodField()

    class Meta:
        model = StrainModel
        fields = [
            'ReceivedFrom', 'Depositor', 'ReceivedAs', 'ReceivedDate', 'AccessionDate',
            'TypeOfSubstrate', 'IsolatedFrom', 'AnatomicPart', 'Location', 'Geographics',
            'Country', 'USSR', 'CollectedBy', 'CollectedDate', 'IsolationDate',
            'IsolatedBy', 'IsolateNumber', 'IdentificateBy', 'IdentificateDate'
        ]

    def get_ReceivedFrom(self, obj):
        return {'en': obj.ReceivedFromEng, 'ru': obj.ReceivedFromRus}

    def get_Depositor(self, obj):
        return {'en': obj.DepositorEng, 'ru': obj.DepositorRus}

    def get_TypeOfSubstrate(self, obj):
        return {'en': obj.TypeOfSubstrateEng, 'ru': obj.TypeOfSubstrateRus}

    def get_IsolatedFrom(self, obj):
        return {'en': obj.IsolatedFromEng, 'ru': obj.IsolatedFromRus}

    def get_AnatomicPart(self, obj):
        return {'en': obj.AnatomicPartEng, 'ru': obj.AnatomicPartRus}

    def get_Location(self, obj):
        return {'en': obj.LocationEng, 'ru': obj.LocationRus}

    def get_Geographics(self, obj):
        return {'en': obj.GeographicsEng, 'ru': obj.GeographicsRus}

    def get_Country(self, obj):
        return {'en': obj.CountryEng, 'ru': obj.CountryRus}

    def get_CollectedBy(self, obj):
        return {'en': obj.CollectedByEng, 'ru': obj.CollectedByRus}

    def get_IsolatedBy(self, obj):
        return {'en': obj.IsolatedByEng, 'ru': obj.IsolatedByRus}

    def get_IsolateNumber(self, obj):
        return {'en': obj.IsolateNumberEng, 'ru': obj.IsolateNumberRus}

    def get_IdentificateBy(self, obj):
        return {'en': obj.IdentificateByEng, 'ru': obj.IdentificateByRus}

class Section3Serializer(serializers.ModelSerializer):
    GrowthCondition = serializers.SerializerMethodField()

    class Meta:
        model = StrainModel
        fields = [
            'IncubationTemp', 'Tested_temperature_growth_range', 'GrowthMedium',
            'GrowthCondition', 'StorageMethods', 'StorageFreeze', 'StorageOil',
            'StorageSilicagel', 'StorageWater', 'StorageNitrogen',
            'StorageSubcultivation', 'StorageSoil'
        ]

    def get_GrowthCondition(self, obj):
        return {
            'en': obj.GrowthConditionEng,
            'ru': obj.GrowthConditionRus
        }

class Section4Serializer(serializers.ModelSerializer):
    EnzymeProduction = serializers.SerializerMethodField()
    MetaboliteProduction = serializers.SerializerMethodField()
    Transformation = serializers.SerializerMethodField()
    Degradation = serializers.SerializerMethodField()
    Other = serializers.SerializerMethodField()

    class Meta:
        model = StrainModel
        fields = [
            'EnzymeProduction', 'MetaboliteProduction', 'Transformation', 'Degradation',
            'Other', 'MatingType', 'DNA_Sequence_Accession_Numbers'
        ]

    def get_EnzymeProduction(self, obj):
        return {'en': obj.EnzymeProductionEng, 'ru': obj.EnzymeProductionRus}

    def get_MetaboliteProduction(self, obj):
        return {'en': obj.MetaboliteProductionEng, 'ru': obj.MetaboliteProductionRus}

    def get_Transformation(self, obj):
        return {'en': obj.TransformationEng, 'ru': obj.TransformationRus}

    def get_Degradation(self, obj):
        return {'en': obj.DegradationEng, 'ru': obj.DegradationRus}

    def get_Other(self, obj):
        return {'en': obj.OtherEng, 'ru': obj.OtherRus}


class Section5Serializer(serializers.ModelSerializer):
    Reidentif = serializers.SerializerMethodField()
    Application = serializers.SerializerMethodField()

    class Meta:
        model = StrainModel
        fields = [
            'Latitude', 'Longitude', 'Altitude', 'Curator', 'Category',
            'Restrictions_on_use', 'Remarks', 'EntryDate', 'EditDate',
            'Reidentif', 'Confidential_Information', 'Application',
            'Form_of_supply', 'Report2020', 'Report2021'
        ]

    def get_Reidentif(self, obj):
        return {'en': obj.ReidentifEng, 'ru': obj.ReidentifRus}

    def get_Application(self, obj):
        return {'en': obj.ApplicationEng, 'ru': obj.ApplicationRus}

class PreviewSectionSerializer(serializers.ModelSerializer):
    TypeOfSubstrate = serializers.SerializerMethodField()
    Country = serializers.SerializerMethodField()
    class Meta:
        model = StrainModel
        fields = ['CollectionCode', 'Strain', 'Genus', 'Species', 'Variant', 'AuthoritySp', 'TypeOfSubstrate', 'Country', 'IsolationDate']

    def get_TypeOfSubstrate(self, obj):
        return {
            'en': obj.TypeOfSubstrateEng,
            'ru': obj.TypeOfSubstrateRus
        }

    def get_Country(self, obj):
        return {
            'en': obj.CountryEng,
            'ru': obj.CountryRus
        }

    def get_IsolationDate(self, obj):
        if obj.IsolationDate:
            return obj.IsolationDate
        elif obj.ReceivedDate:
            return obj.ReceivedDate
        else:
            return None

class AddStrainSerializer(serializers.ModelSerializer):
    class Meta:
        model = StrainModel
        fields = '__all__'

class PreviewStrainSerializer(serializers.ModelSerializer):
    PreviewSection = PreviewSectionSerializer(read_only=True)
    class Meta:
        model = StrainModel
        fields = ['strain_id', 'PreviewSection']

class StrainChangeSerializer(serializers.ModelSerializer):
    strain = PreviewStrainSerializer(read_only=True)
    changed_by = UserSerializer(read_only=True)
    class Meta:
        model = StrainChangeModel
        fields = '__all__'

class StrainSerializer(serializers.ModelSerializer):
    Section1 = Section1Serializer(read_only=True)
    Section2 = Section2Serializer(read_only=True)
    Section3 = Section3Serializer(read_only=True)
    Section4 = Section4Serializer(read_only=True)
    Section5 = Section5Serializer(read_only=True)
    class Meta:
        model = StrainModel
        fields = ['strain_id', 'Section1', 'Section2', 'Section3', 'Section4', 'Section5']

