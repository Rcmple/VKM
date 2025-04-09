from django.contrib.postgres.search import TrigramSimilarity
from django.db.models import Func, F, CharField
from django.db.models.functions import Greatest
from rest_framework.views import APIView
from rest_framework.response import Response
from strains.models import StrainModel
from strains.serializers import PreviewStrainSerializer
import re
from rest_framework.pagination import LimitOffsetPagination
from strains.views import StrainsListPagination


class StrainsSearchView(APIView):
    pagination_class = StrainsListPagination
    def get(self, request):
        cur_query = request.query_params.get('q', None)

        if not cur_query:
            return Response({
                'error': {
                    'ru': 'Параметр q не найден',
                    'en': 'Parameter q not found'
                }
            }, status=400)

        words = re.findall(r'\w+', cur_query)

        if not words:
            return Response({'error': 'Введите корректный запрос'}, status=400)

        strains = StrainModel.objects.annotate(
            strain_text=Func(
                F('Strain'),
                function='CAST',
                template='CAST(%(expressions)s AS TEXT)',
                output_field=CharField()
            )
        )

        for word in words:
            strains = strains.annotate(
                similarity=Greatest(
                    TrigramSimilarity('Genus', word),
                    TrigramSimilarity('Species', word),
                    TrigramSimilarity('strain_text', word)
                )
            ).filter(similarity__gt=0.2)

        strains = strains.annotate(
            total_similarity=sum([
                Greatest(
                    TrigramSimilarity('Genus', word),
                    TrigramSimilarity('Species', word)
                ) for word in words
            ])
        ).order_by('-total_similarity')

        paginator = self.pagination_class()
        result_page = paginator.paginate_queryset(strains, request)
        serializer = PreviewStrainSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)
