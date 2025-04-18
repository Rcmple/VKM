from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.search import SearchVectorField
from django.contrib.postgres.indexes import GinIndex


class StrainModel(models.Model):
    strain_id = models.AutoField(primary_key=True, verbose_name="Счетчик")

    # Раздел 1 – Наименование штамма, таксономия, номенклатура, степень риска
    CollectionCode = models.CharField(max_length=255, null=True, verbose_name="CollectionCode")
    Subcollection = models.CharField(max_length=255, null=True, verbose_name="Subcollection")
    Subcollection1 = models.CharField(max_length=255, null=True, verbose_name="Subcollection1")
    Genus = models.CharField(max_length=255, null=True, verbose_name="Genus")
    Species = models.CharField(max_length=255, null=True, verbose_name="Species")
    Variant = models.CharField(max_length=255, blank=True, null=True, verbose_name="Variant")
    Forma = models.CharField(max_length=255, blank=True, null=True, verbose_name="Forma")
    FormaSpecies = models.CharField(max_length=255, blank=True, null=True, verbose_name="FormaSpecies")
    Strain = models.IntegerField(verbose_name="Strain", null=True,)
    AuthoritySp = models.CharField(max_length=255, null=True, verbose_name="AuthoritySp")
    AuthoritySubSp = models.CharField(max_length=255, blank=True, null=True, verbose_name="AuthoritySubSp")
    Family = models.CharField(max_length=255, blank=True, null=True, verbose_name="Family")
    Order = models.CharField(max_length=255, blank=True, null=True, verbose_name="Order")
    Class = models.CharField(max_length=255, blank=True, null=True, verbose_name="Class")
    Synonym = models.TextField(blank=True, null=True, verbose_name="Synonym")
    TaxonomicID = models.IntegerField(blank=True, null=True, verbose_name="TaxonomicID (DSMZ, MycoBank)")
    CurrentName = models.CharField(max_length=255, blank=True, null=True,
                                   verbose_name="Current Name (DSMZ, MycoBank)")
    Link_to_TaxonomicID = models.CharField(max_length=255, blank=True, null=True,
                                           verbose_name="Link to TaxonomicID (DSMZ, MycoBank Website)")
    Pathogenicgroup = models.CharField(max_length=255, blank=True, null=True, verbose_name="Pathogenicgroup (Russian "
                                                                                           "Federation)")
    RiskGroup = models.CharField(max_length=255, blank=True, null=True, verbose_name="Risk group")
    SanPin = models.CharField(max_length=255, blank=True, null=True, verbose_name="SanPin")
    State = models.CharField(max_length=255, blank=True, null=True, verbose_name="State")
    TypeRus = models.CharField(max_length=255, blank=True, null=True, verbose_name="TypeRus")
    TypeEng = models.CharField(max_length=255, blank=True, null=True, verbose_name="TypeEng")
    Qouts = models.CharField(max_length=255, blank=True, null=True, verbose_name="Qouts")
    OtherName = models.CharField(max_length=255, blank=True, null=True, verbose_name="OtherName")
    ClassShort = models.CharField(max_length=255, blank=True, null=True, verbose_name="ClassShort")
    References = models.TextField(blank=True, null=True, verbose_name="References")
    References_nc = models.TextField(blank=True, null=True, verbose_name="References-nc")
    Race = models.CharField(max_length=255, blank=True, null=True, verbose_name="Race")
    Serovar = models.CharField(max_length=255, blank=True, null=True, verbose_name="Serovar")
    OtherCol = models.TextField(blank=True, null=True, verbose_name="OtherCol")

    # Раздел 2 – История штамма
    ReceivedFromRus = models.CharField(max_length=255, null=True, verbose_name="ReceivedFromRus")
    ReceivedFromEng = models.CharField(max_length=255, null=True, verbose_name="ReceivedFromEng")
    DepositorRus = models.CharField(max_length=255, blank=True, null=True, verbose_name="DepositorRus")
    DepositorEng = models.CharField(max_length=255, blank=True, null=True, verbose_name="DepositorEng")
    ReceivedAs = models.CharField(max_length=255, verbose_name="ReceivedAs", null=True)
    ReceivedDate = models.DateField(null=True, blank=True, verbose_name="ReceivedDate")
    AccessionDate = models.DateField(max_length=255, null=True, blank=True, verbose_name="AccessionDate")
    TypeOfSubstrateRus = models.CharField(max_length=255, null=True, verbose_name="TypeOfSubstrateRus")
    TypeOfSubstrateEng = models.CharField(max_length=255, null=True, verbose_name="TypeOfSubstrateEng")
    IsolatedFromRus = models.CharField(max_length=255, null=True, verbose_name="IsolatedFromRus")
    IsolatedFromEng = models.CharField(max_length=255, null=True, verbose_name="IsolatedFromEng")
    AnatomicPartRus = models.CharField(max_length=255, blank=True, null=True, verbose_name="AnatomicPartRus")
    AnatomicPartEng = models.CharField(max_length=255, blank=True, null=True, verbose_name="AnatomicPartEng")
    LocationRus = models.CharField(max_length=255, blank=True, null=True, verbose_name="LocationRus")
    LocationEng = models.CharField(max_length=255, blank=True, null=True, verbose_name="LocationEng")
    GeographicsRus = models.CharField(max_length=255, blank=True, null=True, verbose_name="GeographicsRus")
    GeographicsEng = models.CharField(max_length=255, blank=True, null=True, verbose_name="GeographicsEng")
    CountryRus = models.CharField(max_length=255, blank=True, null=True, verbose_name="CountryRus")
    CountryEng = models.CharField(max_length=255, blank=True, null=True, verbose_name="CountryEng")
    USSR = models.CharField(max_length=255, blank=True, null=True, verbose_name="USSR")
    CollectedByRus = models.CharField(max_length=255, blank=True, null=True, verbose_name="CollectedByRus")
    CollectedByEng = models.CharField(max_length=255, blank=True, null=True, verbose_name="CollectedByEng")
    CollectedDate = models.DateField(null=True, blank=True, verbose_name="CollectedDate")
    IsolationDate = models.DateField(null=True, blank=True, verbose_name="IsolationDate")
    IsolatedByRus = models.CharField(max_length=255, blank=True, null=True, verbose_name="IsolatedByRus")
    IsolatedByEng = models.CharField(max_length=255, blank=True, null=True, verbose_name="IsolatedByEng")
    IsolateNumberRus = models.CharField(max_length=255, blank=True, null=True, verbose_name="IsolateNumberRus")
    IsolateNumberEng = models.CharField(max_length=255, blank=True, null=True, verbose_name="IsolateNumberEng")
    IdentificateByRus = models.CharField(max_length=255, blank=True, null=True, verbose_name="IdentificateByRus")
    IdentificateByEng = models.CharField(max_length=255, blank=True, null=True, verbose_name="IdentificateByEng")
    IdentificateDate = models.CharField(max_length=255, blank=True, null=True, verbose_name="IdentificateDate")

    # Раздел 3 – Культивирование и хранение штамма
    IncubationTemp = models.IntegerField(null=True, verbose_name="IncubationTemp")
    Tested_temperature_growth_range = models.CharField(max_length=255, blank=True, null=True,
                                                       verbose_name="Tested temperature growth range")
    GrowthMedium = models.IntegerField(null=True, verbose_name="GrowthMedium")
    GrowthConditionRus = models.CharField(max_length=255, blank=True, null=True, verbose_name="GrowthConditionRus")
    GrowthConditionEng = models.CharField(max_length=255, blank=True, null=True, verbose_name="GrowthConditionEng")
    StorageMethods = models.CharField(max_length=255, verbose_name="StorageMethods", null=True)
    StorageFreeze = models.CharField(max_length=255, blank=True, null=True, verbose_name="StorageFreeze")
    StorageOil = models.CharField(max_length=255, blank=True, null=True, verbose_name="StorageOil")
    StorageSilicagel = models.CharField(max_length=255, blank=True, null=True, verbose_name="StorageSilicagel")
    StorageWater = models.CharField(max_length=255, blank=True, null=True, verbose_name="StorageWater")
    StorageNitrogen = models.CharField(max_length=255, blank=True, null=True, verbose_name="StorageNitrogen")
    StorageSubcultivation = models.CharField(max_length=255, blank=True, null=True, verbose_name="StorageSubcultivation")
    StorageSoil = models.CharField(max_length=255, blank=True, null=True, verbose_name="StorageSoil")

    # Раздел 4 – Характеристика штамма
    EnzymeProductionEng = models.CharField(max_length=255, blank=True, null=True, verbose_name="EnzymeProductionEng")
    MetaboliteProductionEng = models.CharField(max_length=255, blank=True, null=True, verbose_name="MetaboliteProductionEng")
    TransformationEng = models.CharField(max_length=255, blank=True, null=True, verbose_name="TransformationEng")
    DegradationEng = models.CharField(max_length=255, blank=True, null=True, verbose_name="DegradationEng")
    OtherRus = models.TextField(blank=True, null=True, verbose_name="OtherRus")
    OtherEng = models.TextField(blank=True, null=True, verbose_name="OtherEng")
    MatingType = models.CharField(max_length=255, blank=True, null=True, verbose_name="MatingType")
    DNA_Sequence_Accession_Numbers = models.CharField(max_length=255, blank=True, null=True,
                                                      verbose_name="DNA Sequence Accession Numbers")

    # Раздел 5 – Общая информация

    Latitude = models.CharField(max_length=255, blank=True, null=True, verbose_name="Latitude")
    Longitude = models.CharField(max_length=255, blank=True, null=True, verbose_name="Longitude")
    Altitude = models.CharField(max_length=255, blank=True, null=True, verbose_name="Altitude")
    Curator = models.CharField(max_length=255, null=True, verbose_name="Curator")
    Category = models.CharField(max_length=255, null=True, blank=True, verbose_name="Category")
    Restrictions_on_use = models.CharField(max_length=255, blank=True, null=True, verbose_name="Restrictions on use")
    Remarks = models.CharField(max_length=255, verbose_name="Remarks")
    EntryDate = models.DateField(null=True, blank=True, verbose_name="EntryDate")
    EditDate = models.DateField(null=True, blank=True, verbose_name="EditDate")
    ReidentifRus = models.CharField(max_length=255, blank=True, null=True, verbose_name="ReidentifRus")
    ReidentifEng = models.CharField(max_length=255, blank=True, null=True, verbose_name="ReidentifEng")
    Confidential_Information = models.CharField(max_length=255, blank=True, null=True, verbose_name="Confidential Information")
    ApplicationRus = models.CharField(max_length=255, blank=True, null=True, verbose_name="ApplicationRus")
    ApplicationEng = models.CharField(max_length=255, blank=True, null=True, verbose_name="ApplicationEng")
    Form_of_supply = models.CharField(max_length=255, blank=True, null=True, verbose_name="Form of supply")
    Report2020 = models.CharField(max_length=255, blank=True, null=True, verbose_name="Report2020")
    Report2021 = models.CharField(max_length=255, blank=True, null=True, verbose_name="Report2021")
    EnzymeProductionRus = models.CharField(max_length=255, blank=True, null=True, verbose_name="EnzymeProductionRus")
    MetaboliteProductionRus = models.CharField(max_length=255, blank=True, null=True, verbose_name="MetaboliteProductionRus")
    TransformationRus = models.CharField(max_length=255, blank=True, null=True, verbose_name="TransformationRus")
    DegradationRus = models.CharField(max_length=255, blank=True, null=True, verbose_name="DegradationRus")

    #search

    search_taxon_name_vector = SearchVectorField(null=True)
    search_isolated_from_vector = SearchVectorField(null=True)
    search_geographics_vector = SearchVectorField(null=True)
    search_country_vector = SearchVectorField(null=True)
    search_any_vector = SearchVectorField(null=True)

    class Meta:
        verbose_name_plural = 'strains'
        indexes = [GinIndex(fields=['search_taxon_name_vector']),
                   GinIndex(fields=['search_isolated_from_vector']),
                   GinIndex(fields=['search_geographics_vector']),
                   GinIndex(fields=['search_country_vector']),
                   GinIndex(fields=['search_any_vector'])]


class StrainChangeRequestModel(models.Model):
    strain = models.ForeignKey(StrainModel, on_delete=models.CASCADE, related_name='changes')
    changed_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='changes')
    changes = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)
    message = models.TextField(blank=True, null=True)


class StrainNewRequestModel(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='new')
    changes = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)
    message = models.TextField(blank=True, null=True)
