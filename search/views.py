from django.contrib.postgres.search import TrigramSimilarity
from django.db.models.functions import Greatest
from rest_framework.views import APIView
from rest_framework.response import Response
from strains.models import StrainModel
from strains.serializers import PreviewStrainSerializer
import re

class StrainsSearchView(APIView):

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

        strains = StrainModel.objects.all()
        for word in words:
            strains = strains.annotate(
                similarity=Greatest(
                    TrigramSimilarity('Genus', word),
                    TrigramSimilarity('Species', word)
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

        serializer = PreviewStrainSerializer(strains, many=True)
        return Response(serializer.data)

