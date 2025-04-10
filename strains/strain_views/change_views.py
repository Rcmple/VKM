from datetime import datetime
import csv

from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.db.models import F
from django.contrib.postgres.search import SearchVector

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from VKMauth.permissions import IsModerator
from strains.models import StrainModel, StrainChangeRequestModel, StrainNewRequestModel
from strains.serializers import StrainNewRequestSerializer, StrainChangeRequestSerializer, StrainSerializer
from strains.fields_validate import try_validate_changes


def parse_date(date_str):
    if date_str is None:
        return None
    try:
        return datetime.strptime(date_str.strip(), "%m/%d/%Y").date()
    except ValueError:
        return None


class StrainChangeRequestView(APIView):
    permission_classes = [IsAuthenticated]

    # Отправление всех полей для заполнения, а также их текущее значение
    def get(self, request, strain_id_param):
        try:
            strain = StrainModel.objects.get(strain_id=strain_id_param)
        except StrainModel.DoesNotExist:
            return Response({
                'error': {
                    'ru': 'Штамм не найден',
                    'en': 'Strain not found'
                }
            }, status=status.HTTP_404_NOT_FOUND)

        serializer = StrainSerializer(strain, context={'user': request.user})
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Добавление заявки на изменение
    def post(self, request, strain_id_param):
        try:
            strain = StrainModel.objects.get(strain_id=strain_id_param)
        except StrainModel.DoesNotExist:
            return Response({
                'error': {
                    'ru': 'Штамм не найден',
                    'en': 'Strain not found'
                }
            }, status=status.HTTP_404_NOT_FOUND)
        serializer = StrainChangeRequestSerializer(data={
            'changes': request.data.get('changes')
        })

        if serializer.is_valid():
            serializer.save(strain=strain, changed_by=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StrainChangeRequestApproveView(APIView):
    permission_classes = [IsModerator]

    # Одобрение заявки на изменение
    def post(self, request, strain_id_param):
        try:
            strain_change_request = StrainChangeRequestModel.objects.get(id=request.data.get('change_request_id'),
                                                                         strain_id=strain_id_param)
        except StrainChangeRequestModel.DoesNotExist:
            return Response({
                'error': {
                    'en': 'Change request not found or does not belong to the given strain',
                    'ru': 'Запрос на изменение не найден или не принадлежит данному штамму'
                }}, status=status.HTTP_404_NOT_FOUND)

        if strain_change_request.approved:
            return Response({
                'error': {
                    'en': 'This change request has already been approved.',
                    'ru': 'Этот запрос на изменение уже был одобрен.'
                }
            }, status=status.HTTP_400_BAD_REQUEST)

        strain = strain_change_request.strain

        for field, value in strain_change_request.changes.items():
            if hasattr(strain, field):
                setattr(strain, field, value)

        strain.save()

        strain_change_request.approved = True
        strain_change_request.message = request.data.get('message')
        strain_change_request.save()

        return Response({
            'message': {
                'en:': 'Change request approved and changes applied to StrainModel',
                'ru': 'Запрос на изменение одобрен и изменения применены к StrainModel'
            }}, status=status.HTTP_200_OK)


class StrainChangeRequestRejectView(APIView):
    permission_classes = [IsModerator]

    # Отклонение заявки на изменение
    def post(self, request, strain_id_param):
        try:
            strain_change_request = StrainChangeRequestModel.objects.get(id=request.data.get('change_request_id'),
                                                                         strain_id=strain_id_param)
        except StrainChangeRequestModel.DoesNotExist:
            return Response({
                'error': {
                    'en': 'Change request not found or does not belong to the given strain',
                    'ru': 'Запрос на изменение не найден или не принадлежит данному штамму'
                }}, status=status.HTTP_404_NOT_FOUND)

        if strain_change_request.approved:
            return Response({
                'error': {
                    'en': 'This change request has already been approved.',
                    'ru': 'Этот запрос на изменение уже был одобрен.'
                }
            }, status=status.HTTP_400_BAD_REQUEST)

        strain_change_request.approved = False
        strain_change_request.message = request.data.get('message')
        return Response({
            'message': {
                'en:': 'Change request rejected',
                'ru': 'Запрос на изменение отклонен'
            }}, status=status.HTTP_200_OK)


class StrainNewRequestView(APIView):
    permission_classes = [IsAuthenticated]

    # Отправление всех полей для заполнения
    def get(self, request):
        serializer = StrainSerializer()
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Добавление заявки на добавление
    def post(self, request):
        serializer = StrainNewRequestSerializer(data={
            'changes': request.data.get('changes')
        })

        if serializer.is_valid():
            serializer.save(created_by=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StrainNewRequestApproveView(APIView):
    permission_classes = [IsModerator]

    # Одобрение заявки на добавление
    def post(self, request):
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


class StrainNewRequestRejectView(APIView):
    permission_classes = [IsModerator]

    # Отклонение заявки на добавление
    def post(self, request):
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

        strain_new_request.approved = False
        strain_new_request.message = request.data.get('message')

        return Response({
            "message": {
                "ru": "Запрос на добавление отклонен",
                "en": "Add request rejected"
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
                    row.pop("strain_id", None)
                    for fld, val in row.items():
                        if val == "":
                            row[fld] = None
                    for date_format in ["ReceivedDate", "AccessionDate", "CollectedDate", "IsolationDate",
                                        "EntryDate", "EditDate"]:
                        if date_format in row:
                            row[date_format] = parse_date(row[date_format])
                    strain = StrainModel(**row)
                    strains.append(strain)
                StrainModel.objects.bulk_create(strains)
                StrainModel.objects.all().update(
                    search_taxon_name_vector=(
                            SearchVector(F('Genus')) + SearchVector(F('Species')) +
                            SearchVector(F('Synonym')) + SearchVector(F('CurrentName'))
                    ),
                    search_isolated_from_vector=(
                            SearchVector(F('IsolatedFromRus')) + SearchVector(F('IsolatedFromEng')) +
                            SearchVector(F('TypeOfSubstrateRus')) + SearchVector(F('TypeOfSubstrateEng')) +
                            SearchVector(F('AnatomicPartRus')) + SearchVector(F('AnatomicPartEng'))
                    ),
                    search_geographics_vector=(
                            SearchVector(F('LocationRus')) + SearchVector(F('LocationEng')) +
                            SearchVector(F('GeographicsRus')) + SearchVector(F('GeographicsEng'))
                    ),
                    search_country_vector=(
                            SearchVector(F('CountryRus')) + SearchVector(F('CountryEng'))
                    ),
                    search_any_vector=(
                            SearchVector(F('Genus')) + SearchVector(F('Species')) +
                            SearchVector(F('Synonym')) + SearchVector(F('CurrentName')) +
                            SearchVector(F('IsolatedFromRus')) + SearchVector(F('IsolatedFromEng')) +
                            SearchVector(F('TypeOfSubstrateRus')) + SearchVector(F('TypeOfSubstrateEng')) +
                            SearchVector(F('AnatomicPartRus')) + SearchVector(F('AnatomicPartEng')) +
                            SearchVector(F('LocationRus')) + SearchVector(F('LocationEng')) +
                            SearchVector(F('GeographicsRus')) + SearchVector(F('GeographicsEng')) +
                            SearchVector(F('CountryRus')) + SearchVector(F('CountryEng')) +
                            SearchVector(F('Strain')) + SearchVector(F('OtherCol'))
                    )
                )
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
