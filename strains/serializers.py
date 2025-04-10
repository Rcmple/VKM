from rest_framework import serializers
from .models import StrainModel, StrainNewRequestModel, StrainChangeRequestModel
from VKMauth.serializers import UserSerializer
from strains.fields_validate import try_validate_changes


class Section1Serializer(serializers.ModelSerializer):
    Type = serializers.SerializerMethodField()
    VKM_number = serializers.SerializerMethodField()

    class Meta:
        model = StrainModel
        fields = [
            'VKM_number', 'Subcollection1', 'Genus', 'Species', 'Variant',
            'Forma', 'FormaSpecies', 'AuthoritySp', 'AuthoritySubSp', 'Family',
            'Order', 'Class', 'Synonym', 'TaxonomicID', 'CurrentName', 'Link_to_TaxonomicID',
            'Pathogenicgroup', 'RiskGroup', 'SanPin', 'State', 'Type', 'Qouts',
            'OtherName', 'ClassShort', 'References', 'References_nc', 'Race', 'Serovar', 'OtherCol'
        ]

    def get_Type(self, obj):
        return {
            'en': obj.TypeEng,
            'ru': obj.TypeRus
        }

    def get_VKM_number(self, obj):
        return {
            'CollectionCode': obj.CollectionCode,
            'Subcollection': obj.Subcollection,
            'Strain': obj.Strain,
        }

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        user = self.context.get('user')
        if not user.is_authenticated:
            fields_to_remove = ['Subcollection1', 'Forma', 'FormaSpecies', 'AuthoritySubSp', 'Synonym', 'State',
                                'Qouts', 'OtherName', 'ClassShort', 'References_nc', 'Race', 'Serovar']
            for field in fields_to_remove:
                representation.pop(field, None)

        return representation


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

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        user = self.context.get('user')
        if not user.is_authenticated:
            fields_to_remove = ['Depositor', 'AccessionDate', 'USSR', 'CollectedBy', 'CollectedDate',
                                'IsolatedBy', 'IdentificateBy', 'IdentificateDate']
            for field in fields_to_remove:
                representation.pop(field, None)
        return representation


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

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        user = self.context.get('user')
        if not user.is_authenticated:
            fields_to_remove = ['Tested_temperature_growth_range', 'StorageMethods', 'StorageFreeze',
                                'StorageOil', 'StorageSilicagel', 'StorageWater', 'StorageNitrogen',
                                'StorageSubcultivation', 'StorageSoil']
            for field in fields_to_remove:
                representation.pop(field, None)
        return representation


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

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        user = self.context.get('user')
        if not user.is_authenticated:
            fields_to_remove = ['Other', 'MatingType']
            for field in fields_to_remove:
                representation.pop(field, None)
        return representation


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


class PreviewStrainSerializer(serializers.ModelSerializer):
    TypeOfSubstrate = serializers.SerializerMethodField()
    Country = serializers.SerializerMethodField()
    VKM_number = serializers.SerializerMethodField()

    class Meta:
        model = StrainModel
        fields = ['strain_id', 'VKM_number', 'Genus', 'Species', 'Variant', 'AuthoritySp',
                  'TypeOfSubstrate', 'Country', 'IsolationDate']

    def get_VKM_number(self, obj):
        return {
            'CollectionCode': obj.CollectionCode,
            'Subcollection': obj.Subcollection,
            'Strain': obj.Strain,
        }

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


class StrainSerializer(serializers.ModelSerializer):
    NameAndTaxonomy = serializers.SerializerMethodField()  # Раздел 1
    History = serializers.SerializerMethodField()  # Раздел 2
    CultivationAndStorage = serializers.SerializerMethodField()  # Раздел 3
    StrainCharacteristics = serializers.SerializerMethodField()  # Раздел 4
    GeneralInformation = serializers.SerializerMethodField()  # Раздел 5

    class Meta:
        model = StrainModel
        fields = [
            'strain_id', 'NameAndTaxonomy', 'History', 'CultivationAndStorage',
            'StrainCharacteristics', 'GeneralInformation'
        ]

    def get_NameAndTaxonomy(self, obj):
        user = self.context.get('user')
        return Section1Serializer(obj, many=False, context={'user': user}).data

    def get_History(self, obj):
        user = self.context.get('user')
        return Section2Serializer(obj, many=False, context={'user': user}).data

    def get_CultivationAndStorage(self, obj):
        user = self.context.get('user')
        return Section3Serializer(obj, many=False, context={'user': user}).data

    def get_StrainCharacteristics(self, obj):
        user = self.context.get('user')
        return Section4Serializer(obj, many=False, context={'user': user}).data

    def get_GeneralInformation(self, obj):
        user = self.context.get('user')
        if user.is_authenticated:
            return Section5Serializer(obj, many=False).data


class StrainChangeRequestSerializer(serializers.ModelSerializer):
    strain = PreviewStrainSerializer(read_only=True)
    changed_by = UserSerializer(read_only=True)

    class Meta:
        model = StrainChangeRequestModel
        fields = ['strain', 'changed_by', 'changes', 'created_at', 'updated_at', 'approved']

    def validate_changes(self, value):
        errors = {}
        try_validate_changes(value, errors)
        if errors:
            raise serializers.ValidationError(errors)
        return value


class StrainNewRequestSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = StrainNewRequestModel
        fields = ['created_by', 'changes', 'created_at', 'updated_at', 'approved']

    def validate_changes(self, value):
        value["CollectionCode"] = "VKM"
        value["SubCollection"] = "F"

        required_fields = [
            'CollectionCode', 'Subcollection', 'Subcollection1', 'Genus', 'Species',
            'Strain', 'ReceivedFromRus', 'ReceivedFromEng',
            'ReceivedAs', 'ReceivedDate', 'TypeOfSubstrateRus', 'TypeOfSubstrateEng',
            'IsolatedFromRus', 'IsolatedFromEng', 'IncubationTemp', 'GrowthMedium',
            'StorageMethods', 'Curator', 'Remarks', 'EntryDate', 'EditDate'
        ]

        errors = {}
        for cur_field in required_fields:
            if cur_field not in value or not value[cur_field]:
                errors[cur_field] = f"Поле '{cur_field}' обязательно для заполнения."

        if 'Species' in value and value['Species'] != 'sp.':
            if 'AuthoritySp' not in value or not value['AuthoritySp']:
                errors['AuthoritySp'] = "Поле 'AuthoritySp' обязательно для заполнения, если 'Species' не равно 'sp.'."

        if errors:
            raise serializers.ValidationError(errors)

        try_validate_changes(value, errors)

        if errors:
            raise serializers.ValidationError(errors)

        return value
