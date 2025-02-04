from django.db import models

# Create your models here.

class Strains(models.Model):
    strain_id = models.AutoField(primary_key=True)
    #Раздел 1 – Наименование штамма, такcономия, номенклатура, степень риска
    CollectionCode = models.CharField(max_length = 255)
    Subcollection = models.CharField(max_length = 255)
    Subcollection1 = models.CharField(max_length = 255)
    Genus = models.CharField(max_length = 255)
    Species = models.CharField(max_length = 255)
    Variant = models.CharField(max_length = 255)
    Forma = models.CharField(max_length = 255)
    FormaSpecies = models.CharField(max_length = 255)
    Strain = models.FloatField()
    AuthoritySp = models.CharField(max_length = 255)
    AuthoritySubSp = models.CharField(max_length = 255)
    Family = models.CharField(max_length = 255)
    Order = models.CharField(max_length = 255)
    Class = models.CharField(max_length = 255)
    Synonym = models.TextField(max_length = 65536)
    TaxonomicID = models.CharField(max_length = 255)
    Current_Name = models.CharField(max_length = 255)
    Link_to_TaxonomicID = models.CharField(max_length = 255)
    Pathogenicgroup = models.CharField(max_length = 255)
    Risk_group = models.CharField(max_length = 255)
    SanPin = models.CharField(max_length = 255)
    State = models.CharField(max_length = 255)
    TypeRus = models.CharField(max_length = 255)
    TypeEng = models.CharField(max_length = 255)
    accepted_name = models.CharField(max_length = 255)
    OtherName = models.CharField(max_length = 255)
    ClassShort = models.CharField(max_length = 255)
    References = models.TextField(max_length = 65536)
    References_nc = models.TextField(max_length = 65536)
    Race = models.CharField(max_length = 255)
    Serovar = models.CharField(max_length = 255)
    OtherCol = models.TextField(max_length = 65536)

    #Раздел 2 – История штамма
    ReceivedFromRus = models.CharField(max_length = 255)
    ReceivedFromEng = models.CharField(max_length = 255)
    DepositorRus = models.CharField(max_length = 255)
    DepositorEng = models.CharField(max_length = 255)
    ReceivedAs = models.CharField(max_length = 255)
    ReceivedDate = models.CharField(max_length = 255)
    AccessionDate = models.CharField(max_length = 255)
    TypeOfSubstrateRus = models.CharField(max_length = 255)
    TypeOfSubstrateEng = models.CharField(max_length = 255)
    IsolatedFromRus = models.CharField(max_length = 255)
    IsolatedFromEng = models.CharField(max_length = 255)
    AnatomicPartRus = models.CharField(max_length = 255)
    AnatomicPartEng = models.CharField(max_length = 255)
    LocationRus = models.CharField(max_length = 255)
    LocationEng = models.CharField(max_length = 255)
    GeographicsRus = models.CharField(max_length = 255)
    GeographicsEng = models.CharField(max_length = 255)
    CountryRus = models.CharField(max_length = 255)
    CountryEng = models.CharField(max_length = 255)
    USSR = models.CharField(max_length = 255)
    CollectedByRus = models.CharField(max_length = 255)
    CollectedByEng = models.CharField(max_length = 255)
    CollectedDate = models.DateField()
    IsolationDate = models.DateField()
    IsolatedByRus = models.CharField(max_length = 255)
    IsolatedByEng = models.CharField(max_length = 255)
    IsolateNumberRus = models.CharField(max_length = 255)
    IsolateNumberEng = models.CharField(max_length = 255)
    IdentificateByRus = models.CharField(max_length = 255)
    IdentificateByEng = models.CharField(max_length = 255)
    IdentificateDate = models.CharField(max_length = 255)

    #Раздел 3 – Культивирование и хранение штамма
    IncubationTemp = models.CharField(max_length = 255)
    Tested_temperature_growth_range = models.CharField(max_length = 255)
    GrowthMedium = models.CharField(max_length = 255)
    GrowthConditionRus = models.CharField(max_length=255)
    GrowthConditionEng = models.CharField(max_length = 255)
    StorageMethods = models.CharField(max_length = 255)
    StorageFreeze = models.CharField(max_length = 255)
    StorageOil = models.CharField(max_length = 255)
    StorageSilicagel = models.CharField(max_length = 255)
    StorageWater = models.CharField(max_length = 255)
    StorageNitrogen = models.CharField(max_length = 255)
    StorageSubcultivation = models.CharField(max_length = 255)
    StorageSoil = models.CharField(max_length = 255)

    #Раздел 4 – Характеристика штамма
    EnzymeProductionEng = models.CharField(max_length = 255)
    MeraboliteProductionEng = models.CharField(max_length = 255)
    TransformationEng = models.CharField(max_length = 255)
    DegradationEng = models.CharField(max_length = 255)
    OtherRus = models.CharField(max_length = 255)
    OtherEng = models.CharField(max_length = 255)
    MatingType = models.CharField(max_length = 255)
    DNA_Sequence_Accession_Numbers = models.CharField(max_length = 255)

    #Раздел 5 – Общая информация
    Latitude = models.CharField(max_length = 255)
    Longitude = models.CharField(max_length = 255)
    Altitude = models.CharField(max_length = 255)
    Curator = models.CharField(max_length = 255)
    Category = models.CharField(max_length = 255)
    Restrictions_on_use = models.CharField(max_length = 255)
    Remarks = models.CharField(max_length = 255)
    EntryDate = models.DateField()
    EditDate = models.DateField()
    ReidentifRus = models.CharField(max_length = 255)
    ReidentifEng = models.CharField(max_length = 255)
    Confidential_Information = models.CharField(max_length = 255)
    ApplicationRus = models.CharField(max_length = 255)
    ApplicationEng = models.CharField(max_length = 255)
    Form_of_supply = models.CharField(max_length = 255)
    Report2020 = models.CharField(max_length = 255)
    Report2021 = models.CharField(max_length = 255)
    EnzymeProductionRus = models.CharField(max_length = 255)
    MeraboliteProductionRus = models.CharField(max_length = 255)
    TransformationRus = models.CharField(max_length = 255)
    DegradationRus = models.CharField(max_length = 255)
    class Meta:
        verbose_name_plural = 'strains'
