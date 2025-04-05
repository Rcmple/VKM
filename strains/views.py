from rest_framework.views import APIView
from .serializers import (StrainNewRequestSerializer,
                          StrainSerializer, PreviewStrainSerializer,
                          StrainChangeRequestSerializer)
from rest_framework.response import Response
from rest_framework import status
from .models import StrainModel, StrainChangeRequestModel, StrainNewRequestModel
import csv
from datetime import datetime
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import LimitOffsetPagination
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

class StrainsListPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 100

class StrainsListView(APIView):
    pagination_class = StrainsListPagination

    def get(self, request):
        if request.user and request.user.groups.filter(name='Moderator').exists():
            strains = StrainModel.objects.all().order_by("strain_id")
        elif request.user:
            strains = StrainModel.objects.filter(Remarks__in=['cat', 'nc', 'ncat', 'dep']).order_by("strain_id")
        else:
            strains = StrainModel.objects.filter(Remarks="cat").order_by("strain_id")

        paginator = self.pagination_class()
        result_page = paginator.paginate_queryset(strains, request)
        serializer = PreviewStrainSerializer(result_page, many=True)

        return paginator.get_paginated_response(serializer.data)

class StrainChangeRequestListView(APIView):
    permission_classes = [IsModerator]
    pagination_class = StrainsListPagination
    def get(self, request):
        change_requests = StrainChangeRequestModel.objects.all()
        paginator = self.pagination_class()
        result_page = paginator.paginate_queryset(change_requests, request)
        serializer = StrainChangeRequestSerializer(result_page, many=True)

        return paginator.get_paginated_response(serializer.data)

class StrainNewRequestListView(APIView):
    permission_classes = [IsModerator]
    def get(self, request):
        new_requests = StrainNewRequestModel.objects.all()
        serializer = StrainNewRequestSerializer(new_requests, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class StrainInfoView(APIView):
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

class StrainChangeRequestView(APIView):
    permission_classes = [IsAuthenticated]
    #это чтобы добавлять измененные в отдельную модель с измененями
    def post(self, request, strain_id):
        serializer = StrainChangeRequestSerializer(data={
            'strain': strain_id,
            'changed_by': request.user.id,
            'changes': request.data.get('changes')
        })

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #это чтобы одобрить изменения и применить их в главной модели
    def put(self, request, strain_id):
        if not request.user.groups.filter(name='Moderator').exists():
            return Response({
                'error': {
                    'en' : 'You do not have permission to approve change requests',
                    'ru' : 'У вас нет прав на одобрение запросов на изменение'
                }}, status=status.HTTP_403_FORBIDDEN)
        try:
            strain_change_request = StrainChangeRequestModel.objects.get(id=request.data.get('change_request_id'),
                                                                         strain_id=strain_id)
        except StrainChangeRequestModel.DoesNotExist:
            return Response({
                'error': {
                    'en' : 'Change request not found or does not belong to the given strain',
                    'ru' : 'Запрос на изменение не найден или не принадлежит данному штамму'
                }}, status=status.HTTP_404_NOT_FOUND)

        if strain_change_request.approved:
            return Response({
                'error': {
                    'en' : 'This change request has already been approved.',
                    'ru' : 'Этот запрос на изменение уже был одобрен.'
                }
            }, status=status.HTTP_400_BAD_REQUEST)

        strain = strain_change_request.strain

        for field, value in strain_change_request.changes.items():
            if hasattr(strain, field):
                setattr(strain, field, value)

        strain.save()

        strain_change_request.approved = True
        strain_change_request.save()

        return Response({
            'message': {
                'en:' : 'Change request approved and changes applied to StrainModel',
                'ru' : 'Запрос на изменение одобрен и изменения применены к StrainModel'
            }}, status=status.HTTP_200_OK)

class StrainNewRequestView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = StrainNewRequestSerializer(data={
            'created_by': request.user.id,
            'changes': request.data.get('changes')
        })

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self, request):
        try:
            strain_new_request = StrainNewRequestModel.objects.get(id=request.data.get('new_request_id'))
        except StrainNewRequestModel.DoesNotExist:
            return Response({
                "error": {
                "ru": "Запрос на добавление не найден или не принадлежит данному штамму",
                "en": "Add request not found or does not belong to this strain"
                }
            }, status=status.HTTP_404_NOT_FOUND)

        if strain_new_request.approved:
            return Response({
                "error": {
                "ru": "Этот запрос на добавление уже был одобрен",
                "en": "This add request has already been approved"
             }
            }, status=status.HTTP_400_BAD_REQUEST)

        strain = StrainModel.objects.create(**strain_new_request.changes)
        strain.save()

        strain_new_request.approved = True
        strain_new_request.save()

        return Response({
            "message": {
                "ru": "Запрос на добавление одобрен и новый штамм добавлен в StrainModel",
                "en": "Add request approved and new strain added to StrainModel"
            }
        }, status=status.HTTP_200_OK)


class StrainsUploadRequestView(APIView):
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
