from rest_framework.views import APIView
from .serializers import AddStrainSerializer, StrainSerializer, PreviewStrainSerializer, StrainChangeSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import StrainModel, StrainChangeModel
import csv
from datetime import datetime
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from VKMauth.permissions import IsModerator


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


class StrainsListView(APIView):
    def get(self, request):
        if request.user and request.user.groups.filter(name='Moderator').exists():
            # Показываю все штаммы, так как админ
            strains = StrainModel.objects.all().order_by("strain_id")
            serializer = PreviewStrainSerializer(strains, many=True)
            return Response(serializer.data)
        elif request.user:
            strains = StrainModel.objects.filter(Remarks__in=['cat', 'nc', 'ncat', 'dep']).order_by("strain_id")
            serializer = PreviewStrainSerializer(strains, many=True)
            print(serializer.data)
            return Response(serializer.data)
        else:
            # Показываю только те на которых метка "cat"
            strains = StrainModel.objects.filter(Remarks="cat").order_by("strain_id")
            serializer = PreviewStrainSerializer(strains, many=True)
            return Response(serializer.data)


class EditedStrainsListView(APIView):
    permission_classes = [IsModerator]

    def get(self, request):
        suggestions = StrainChangeModel.objects.all()
        serializer = StrainChangeSerializer(suggestions, many=True)
        return Response(serializer.data)

class StrainView(APIView):

    def get(self, request, strain_id):
        #Беру всю информацию о Штамме
        try:
            strain = StrainModel.objects.get(strain_id=strain_id)
        except StrainModel.DoesNotExist:
            return Response({
                'error': {
                    'ru': 'Штамм не найден',
                    'en': 'Strain not found'
                }
            }, status=status.HTTP_404_NOT_FOUND)
        if strain.Remarks != "cat" and not request.user:
            return Response({
                'error': {
                    'ru': 'Штамм не найден',
                    'en': 'Strain not found'
                }
            }, status=status.HTTP_404_NOT_FOUND)
        serializer = StrainSerializer(strain)
        return Response(serializer.data, status=status.HTTP_200_OK)

class EditedStrainView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, strain_id):
        try:
            strain = StrainModel.objects.get(strain_id=strain_id)
        except StrainModel.DoesNotExist:
            return Response({
                'error': {
                    'ru': 'Штамм не найден',
                    'en': 'Strain not found'
                }
            }, status=status.HTTP_404_NOT_FOUND)

        change = StrainChangeModel.objects.create(
            strain=strain,
            changes=request.data,
            changed_by=request.user
        )

        return Response({
            'message': {
                'ru': 'Изменения успешно предложены',
                'en': 'Changes successfully suggested'
            }
        }, status=status.HTTP_201_CREATED)

class AddStrainView(APIView):
    def post(self, request):
        serializer = AddStrainSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': {
                    'ru': 'Штамм успешно добавлен',
                    'en': 'Strain successfully added'
                },
                'strain_id': serializer.data['id']
            }, status=status.HTTP_201_CREATED)
        else:
            return Response({
                'error': {
                    'ru': serializer.errors,
                    'en': serializer.errors
                }
            }, status=status.HTTP_400_BAD_REQUEST)


class UploadStrainsView(APIView):
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
                    strain = StrainModel(
                        CollectionCode=row.get("CollectionCode", ""),
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
                        Family=row.get("Family", ""),
                        Order=row.get("Order", ""),
                        Class=row.get("Class", ""),
                        Synonym=row.get("Synonym", ""),
                        TaxonomicID=row.get("TaxonomicID", ""),
                        Current_Name_DSMZ_MycoBank=row.get("Current_Name", ""),
                        Link_to_TaxonomicID=row.get("Link_to_TaxonomicID", ""),
                        Pathogenicgroup=row.get("Pathogenicgroup", ""),
                        Risk_group=row.get("Risk_group", ""),
                        SanPin=row.get("SanPin", ""),
                        State=row.get("State", ""),
                        TypeRus=row.get("TypeRus", ""),
                        TypeEng=row.get("TypeEng", ""),
                        Qouts=row.get("Qouts", ""),
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
                    strain.TypeOfSubstrateRus = row.get("TypeOfSubstrateRus", "")
                    strain.TypeOfSubstrateEng = row.get("TypeOfSubstrateEng", "")
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
                    strain.Tested_temperature_growth_range = row.get("Tested_temperature_growth_range", "")
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
                    strain.MetaboliteProductionEng = row.get("MetaboliteProductionEng", "")
                    strain.TransformationEng = row.get("TransformationEng", "")
                    strain.DegradationEng = row.get("DegradationEng", "")
                    strain.OtherRus = row.get("OtherRus", "")
                    strain.OtherEng = row.get("OtherEng", "")
                    strain.MatingType = row.get("MatingType", "")
                    strain.DNA_Sequence_Accession_Numbers = row.get("DNA_Sequence_Accession_Numbers", "")

                    # Раздел 5 – Общая информация
                    strain.Latitude = row.get("Latitude", "")
                    strain.Longitude = row.get("Longitude", "")
                    strain.Altitude = row.get("Altitude", "")
                    strain.Curator = row.get("Curator", "")
                    strain.Category = row.get("Category", "")
                    strain.Restrictions_on_use = row.get("Restrictions_on_use", "")
                    strain.Remarks = row.get("Remarks", "")
                    strain.EntryDate = parse_date(row.get("EntryDate", ""))
                    strain.EditDate = parse_date(row.get("EditDate", ""))
                    strain.ReidentifRus = row.get("ReidentifRus", "")
                    strain.ReidentifEng = row.get("ReidentifEng", "")
                    strain.Confidential_Information = row.get("Confidential_Information", "")
                    strain.ApplicationRus = row.get("ApplicationRus", "")
                    strain.ApplicationEng = row.get("ApplicationEng", "")
                    strain.Form_of_supply = row.get("Form_of_supply", "")
                    strain.Report2020 = row.get("Report2020", "")
                    strain.Report2021 = row.get("Report2021", "")
                    strain.EnzymeProductionRus = row.get("EnzymeProductionRus", "")
                    strain.MetaboliteProductionRus = row.get("MetaboliteProductionRus", "")
                    strain.TransformationRus = row.get("TransformationRus", "")
                    strain.DegradationRus = row.get("DegradationRus", "")
                    strains.append(strain)

                StrainModel.objects.bulk_create(strains)
        except Exception as e:
            print(f"⚠️ Ошибка загрузки файла: {e}")
            return Response({"error": {
                'ru': "Ошибка загрузки файла",
                'en': "Error uploading file"}},
                status=status.HTTP_400_BAD_REQUEST)
        return Response({"message": {
            'ru': "Файл успешно загружен",
            'en': "File successfully uploaded"}},
            status=status.HTTP_201_CREATED)
