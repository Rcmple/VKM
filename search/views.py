from django.db.models.functions import Cast
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from rest_framework.response import Response
from strains.serializers import PreviewStrainSerializer
from strains.strain_views.list_views import StrainsListPagination, get_all_strains
from django.contrib.postgres.search import SearchQuery, SearchRank, TrigramSimilarity
from django.db.models import F
from django.db import models


class StrainsSearchView(APIView):
    pagination_class = StrainsListPagination

    def get(self, request):
        query_data = request.GET
        if query_data is None:
            return Response({
                'error': {
                    'en': 'Query parameter is required',
                    'ru': 'Параметр запроса обязателен'
                }
            }, status=HTTP_400_BAD_REQUEST)

        strain_query = query_data.get('Strain', None)
        taxon_name_query = query_data.get('TaxonName', None)
        status_of_strain_query = query_data.get('StatusOfStrain', None)
        other_col_query = query_data.get('OtherCol', None)
        isolated_from_query = query_data.get('IsolatedFrom', None)
        geographics_query = query_data.get('Geographics', None)
        country_query = query_data.get('Country', None)
        any_query = query_data.get('Any', None)

        strains = get_all_strains(request)
        if strain_query:
            strains = strains.annotate(
                strain_similarity=TrigramSimilarity(Cast(F('Strain'), output_field=models.TextField()), strain_query)
            ).filter(strain_similarity__gt=0.3).order_by('-strain_similarity')
        if taxon_name_query:
            taxon_name_search_query = SearchQuery(taxon_name_query)
            strains = strains.annotate(
                taxon_name_rank=SearchRank(F('search_taxon_name_vector'), taxon_name_search_query)
            ).order_by('-taxon_name_rank')

        if status_of_strain_query == 'type':
            strains = strains.filter(TypeEng__isnull=False)

        if other_col_query:
            strains = strains.annotate(
                other_col_similarity=TrigramSimilarity('OtherCol', other_col_query)
            ).filter(other_col_similarity__gt=0.3).order_by('-other_col_similarity')

        if isolated_from_query:
            isolated_from_search_query = SearchQuery(isolated_from_query)
            strains = strains.annotate(
                isolated_from_rank=SearchRank(F('search_isolated_from_vector'), isolated_from_search_query)
            ).order_by('-isolated_from_rank')

        if geographics_query:
            geographics_search_query = SearchQuery(geographics_query)
            strains = strains.annotate(
                geographics_rank=SearchRank(F('search_geographics_vector'), geographics_search_query)
            ).order_by('-geographics_rank')

        if country_query:
            country_search_query = SearchQuery(country_query)
            strains = strains.annotate(
                country_rank=SearchRank(F('search_country_vector'), country_search_query)
            ).order_by('-country_rank')
        if any_query:
            any_search_query = SearchQuery(any_query)
            strains = strains.annotate(
                any_rank=SearchRank(F('search_any_vector'), any_search_query)
            ).order_by('-any_rank')

        #pagination
        paginator = self.pagination_class()
        result_page = paginator.paginate_queryset(strains, request)
        serializer = PreviewStrainSerializer(result_page, many=True)

        return paginator.get_paginated_response(serializer.data)
