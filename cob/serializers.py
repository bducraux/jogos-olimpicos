from rest_framework import serializers
from .models import Competicao, Atleta, Resultado


class CompeticaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competicao
        fields = ('id', 'nome', 'condicao_para_vitoria', 'status')


class AtletaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Atleta
        fields = ('id', 'nome', 'competicao')


class ResultadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resultado
        fields = ('id', 'atleta', 'competicao', 'resultado')
