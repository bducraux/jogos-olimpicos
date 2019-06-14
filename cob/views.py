from django.shortcuts import render
from rest_framework import viewsets
from .models import Competicao, Atleta, Resultado
from .serializers import CompeticaoSerializer, AtletaSerializer, ResultadoSerializer


class CompeticaoView(viewsets.ModelViewSet):
    queryset = Competicao.objects.all()
    serializer_class = CompeticaoSerializer


class AtletaView(viewsets.ModelViewSet):
    queryset = Atleta.objects.all()
    serializer_class = AtletaSerializer


class ResultadoView(viewsets.ModelViewSet):
    queryset = Resultado.objects.all()
    serializer_class = ResultadoSerializer
