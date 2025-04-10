from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from VKMauth.permissions import IsModerator
from strains.serializers import (StrainSerializer, PreviewStrainSerializer,
                                 StrainNewRequestSerializer, StrainChangeRequestSerializer)
from strains.models import StrainModel, StrainChangeRequestModel, StrainNewRequestModel


def get_all_strains(request):
    if request.user and request.user.groups.filter(name='Moderator').exists():
        strains = StrainModel.objects.all().order_by("strain_id")
    elif request.user.is_authenticated:
        strains = StrainModel.objects.filter(Remarks__in=['cat', 'nc', 'ncat', 'dep']).order_by("strain_id")
    else:
        strains = StrainModel.objects.filter(Remarks="cat").order_by("strain_id")

    return strains


class StrainsListPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 100


class StrainInfoView(APIView):
    def get(self, request, strain_id_param):
        # Беру всю информацию о Штамме
        try:
            strain = StrainModel.objects.get(strain_id=strain_id_param)
        except StrainModel.DoesNotExist:
            return Response({
                'error': {
                    'ru': 'Штамм не найден',
                    'en': 'Strain not found'
                }
            }, status=status.HTTP_404_NOT_FOUND)
        if strain.Remarks != "cat" and not request.user.is_authenticated:
            return Response({
                'error': {
                    'ru': 'Штамм не найден',
                    'en': 'Strain not found'
                }
            }, status=status.HTTP_404_NOT_FOUND)
        serializer = StrainSerializer(strain, context={'user': request.user})
        return Response(serializer.data, status=status.HTTP_200_OK)


class StrainsListView(APIView):
    pagination_class = StrainsListPagination

    def get(self, request):
        strains = get_all_strains(request)

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


class MyStrainChangeRequestListView(APIView):
    permission_classes = [IsAuthenticated]
    pagination_class = StrainsListPagination

    def get(self, request):
        my_change_request_list = StrainChangeRequestModel.objects.filter(changed_by=request.user.id)
        paginator = self.pagination_class()
        result_page = paginator.paginate_queryset(my_change_request_list, request)
        serializer = StrainChangeRequestSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)


class StrainNewRequestListView(APIView):
    permission_classes = [IsModerator]
    pagination_class = StrainsListPagination

    def get(self, request):
        new_requests = StrainNewRequestModel.objects.all()
        paginator = self.pagination_class()
        result_page = paginator.paginate_queryset(new_requests, request)
        serializer = StrainNewRequestSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)


class MyStrainNewRequestListView(APIView):
    permission_classes = [IsAuthenticated]
    pagination_class = StrainsListPagination

    def get(self, request):
        my_new_request_list = StrainNewRequestModel.objects.filter(created_by=request.user.id)
        paginator = pagination_class()
        result_page = paginator.paginate_queryset(my_new_request_list, request)
        serializer = StrainNewRequestSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)
