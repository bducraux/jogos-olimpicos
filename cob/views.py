from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Competicao, Atleta, Resultado
from .serializers import CompeticaoSerializer, AtletaSerializer, ResultadoSerializer, RankingSerializer


class CompeticaoView(viewsets.ModelViewSet):
    queryset = Competicao.objects.all()
    serializer_class = CompeticaoSerializer
    search_fields = ('status', 'condicao_para_vitoria')


class AtletaView(viewsets.ModelViewSet):
    queryset = Atleta.objects.all()
    serializer_class = AtletaSerializer


class ResultadoView(viewsets.ModelViewSet):
    queryset = Resultado.objects.all()
    serializer_class = ResultadoSerializer


class RankingView(APIView):
    """
    Exibe o ranking de uma determinada competição
    """
    def get(self, request, pk):
        resultados = Resultado.pegar_rank_da_competicao(pk)

        serializer = RankingSerializer(resultados, many=True)
        return Response(serializer.data)

