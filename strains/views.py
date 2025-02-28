from rest_framework.views import APIView
from .serializers import AddStrainSerializer, StrainSerializer, PreviewStrainsSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Strain
import csv
from datetime import datetime
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

def parse_date(date_str):
    if not date_str or date_str.lower() in ["null", "deleted", "nc"]:
        return None
    date_formats = ["%d.%m.%Y", "%m/%d/%Y", "%Y-%m-%d"]

    for fmt in date_formats:
        try:
            return datetime.strptime(date_str.strip(), fmt).date()
        except ValueError:
            continue
    return None

class StrainInfoView(APIView):
    def get(self, request, strain_id):
        strain = get_object_or_404(Strain, strain_id=strain_id)
        serializer = StrainSerializer(strain)
        return Response(serializer.data, status=status.HTTP_200_OK)
class AddStrainView(APIView):
    def post(self, request):
        serializer = AddStrainSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message':{
                    'ru':'Штамм успешно добавлен',
                    'en':'Strain successfully added'
                },
                'StrainID' : serializer.data['id']
            }, status = status.HTTP_201_CREATED)
        else:
            return Response({
                'error':{
                    'ru': serializer.errors,
                    'en': serializer.errors
                }
            }, status=status.HTTP_400_BAD_REQUEST)


class StrainsListView(APIView):
    def get(self, request):
        strains = Strain.objects.filter(Remarks="cat").order_by("strain_id")
        serializer = PreviewStrainsSerializer(strains, many=True)
        return Response(serializer.data)
class UploadStrainsView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]
    def post(self, request):
        if "csv_file" not in request.FILES:
            return Response({"error": "Файл не найден"}, status=status.HTTP_400_BAD_REQUEST)
        cur_csv_file = request.FILES["csv_file"]
        if not cur_csv_file.name.endswith('.csv'):
            return Response({"error": "Файл должен быть в формате CSV"}, status=status.HTTP_400_BAD_REQUEST)

        file_path = default_storage.save("temp/" + cur_csv_file.name, ContentFile(cur_csv_file.read()))

        try:
            with open(default_storage.path(file_path), newline='', encoding="utf-8") as file:
                reader = csv.DictReader(file)
                strains = []
                for row in reader:
                    strain = Strain(
                        # Раздел 1 – Наименование штамма, такcономия, номенклатура, степень риска
                        CollectionCode=row.get("collectionCode", ""),
                        Subcollection=row.get("Subcollection", ""),
                        Subcollection1=row.get("Subcollection1", ""),
                        Genus=row.get("Genus", ""),
                        Species=row.get("Species", ""),
                        Variant=row.get("Variant", ""),
                        Forma=row.get("Forma", ""),
                        FormaSpecies=row.get("FormaSpecies", ""),
                        Strain=row.get("Strain", ""),
                        AuthoritySp=row.get("AuthoritySp", ""),
                        AuthoritySubSp=row.get("AuthoritySubSp", ""),
                        Family=row.get("family", ""),
                        Order=row.get("order", ""),
                        Class=row.get("class", ""),
                        Synonym=row.get("Synonym", ""),
                        TaxonomicID=row.get("NameID", ""),
                        Current_Name=row.get("CurrentName", ""),
                        Link_to_TaxonomicID=row.get("Website", ""),
                        Pathogenicgroup=row.get("GruppaPat", ""),
                        Risk_group=row.get("Risk group", ""),
                        SanPin=row.get("SanPin", ""),
                        State=row.get("State", ""),
                        TypeRus=row.get("TypeRus", ""),
                        TypeEng=row.get("TypeEng", ""),
                        accepted_name=row.get("CurrentName", ""),
                        OtherName=row.get("OtherName", ""),
                        ClassShort=row.get("ClassShort", ""),
                        References=row.get("References", ""),
                        References_nc=row.get("References-nc", ""),
                        Race=row.get("Race", ""),
                        Serovar=row.get("Serovar", ""),
                        OtherCol=row.get("OtherCol", ""),
                    )

                    # Раздел 2 – История штамма
                    strain.ReceivedFromRus = row.get("ReceivedFromRus", "")
                    strain.ReceivedFromEng = row.get("ReceivedFromEng", "")
                    strain.DepositorRus = row.get("DepositorRus", "")
                    strain.DepositorEng = row.get("DepositorEng", "")
                    strain.ReceivedAs = row.get("ReceivedAs", "")
                    strain.ReceivedDate = parse_date(row.get("ReceivedDate", ""))
                    strain.AccessionDate = parse_date(row.get("AccessionDate", ""))
                    strain.TypeOfSubstrateRus = row.get("TypeSubstrateRus", "")
                    strain.TypeOfSubstrateEng = row.get("TypeSubstrateEng", "")
                    strain.IsolatedFromRus = row.get("IsolatedFromRus", "")
                    strain.IsolatedFromEng = row.get("IsolatedFromEng", "")
                    strain.AnatomicPartRus = row.get("AnatomicPartRus", "")
                    strain.AnatomicPartEng = row.get("AnatomicPartEng", "")
                    strain.LocationRus = row.get("LocationRus", "")
                    strain.LocationEng = row.get("LocationEng", "")
                    strain.GeographicsRus = row.get("GeographicsRus", "")
                    strain.GeographicsEng = row.get("GeographicsEng", "")
                    strain.CountryRus = row.get("CountryRus", "")
                    strain.CountryEng = row.get("CountryEng", "")
                    strain.USSR = row.get("USSR", "")
                    strain.CollectedByRus = row.get("CollectedByRus", "")
                    strain.CollectedByEng = row.get("CollectedByEng", "")
                    strain.CollectedDate = parse_date(row.get("CollectedDate", ""))
                    strain.IsolationDate = parse_date(row.get("IsolationDate", ""))
                    strain.IsolatedByRus = row.get("IsolatedByRus", "")
                    strain.IsolatedByEng = row.get("IsolatedByEng", "")
                    strain.IsolateNumberRus = row.get("IsolateNumberRus", "")
                    strain.IsolateNumberEng = row.get("IsolateNumberEng", "")
                    strain.IdentificateByRus = row.get("IdentificateByRus", "")
                    strain.IdentificateByEng = row.get("IdentificateByEng", "")
                    strain.IdentificateDate = row.get("IdentificateDate", "")

                    # Раздел 3 – Культивирование и хранение штамма
                    strain.IncubationTemp = row.get("IncubationTemp", "")
                    strain.Tested_temperature_growth_range = row.get("Tested temperature growth range", "")
                    strain.GrowthMedium = row.get("GrowthMedium", "")
                    strain.GrowthConditionRus = row.get("GrowthConditionRus", "")
                    strain.GrowthConditionEng = row.get("GrowthConditionEng", "")
                    strain.StorageMethods = row.get("StorageMethods", "")
                    strain.StorageFreeze = row.get("StorageFreeze", "")
                    strain.StorageOil = row.get("StorageOil", "")
                    strain.StorageSilicagel = row.get("StorageSilicagel", "")
                    strain.StorageWater = row.get("StorageWater", "")
                    strain.StorageNitrogen = row.get("StorageNitrogen", "")
                    strain.StorageSubcultivation = row.get("StorageSubcultivation", "")
                    strain.StorageSoil = row.get("StorageSoil", "")

                    # Раздел 4 – Характеристика штамма
                    strain.EnzymeProductionEng = row.get("EnzymeProductionEng", "")
                    strain.MeraboliteProductionEng = row.get("MeraboliteProductionEng", "")
                    strain.TransformationEng = row.get("TransformationEng", "")
                    strain.DegradationEng = row.get("DegradationEng", "")
                    strain.OtherRus = row.get("OtherRus", "")
                    strain.OtherEng = row.get("OtherEng", "")
                    strain.MatingType = row.get("MatingType", "")
                    strain.DNA_Sequence_Accession_Numbers = row.get("DNASeq", "")

                    # Раздел 5 – Общая информация
                    strain.Latitude = row.get("Latitude", "")
                    strain.Longitude = row.get("Longitude", "")
                    strain.Altitude = row.get("Altitude", "")
                    strain.Curator = row.get("Curator", "")
                    strain.Category = row.get("Category", "")
                    strain.Restrictions_on_use = row.get("Restrictions on use", "")
                    strain.Remarks = row.get("Remarks", "")
                    strain.EntryDate = parse_date(row.get("EntryDate", ""))
                    strain.EditDate = parse_date(row.get("EditDate", ""))
                    strain.ReidentifRus = row.get("ReidentifRus", "")
                    strain.ReidentifEng = row.get("ReidentifEng", "")
                    strain.Confidential_Information = row.get("ConfInf", "")
                    strain.ApplicationRus = row.get("ApplicationRus", "")
                    strain.ApplicationEng = row.get("ApplicationEng", "")
                    strain.Form_of_supply = row.get("Supply", "")
                    strain.Report2020 = row.get("Report2020", "")
                    strain.Report2021 = row.get("Report2021", "")
                    strain.EnzymeProductionRus = row.get("EnzymeProductionRus", "")
                    strain.MeraboliteProductionRus = row.get("MeraboliteProductionRus", "")
                    strain.TransformationRus = row.get("TransformationRus", "")
                    strain.DegradationRus = row.get("DegradationRus", "")
                    strains.append(strain)

                Strain.objects.bulk_create(strains)
        except Exception as e:
            print(f"⚠️ Ошибка загрузки файла: {e}")
            return Response({"error": {
                'ru':"Ошибка загрузки файла",
                'en':"Error uploading file"}},
            status=status.HTTP_400_BAD_REQUEST)
        return Response({"message": {
            'ru':"Файл успешно загружен",
            'en':"File successfully uploaded"}},
            status=status.HTTP_201_CREATED)