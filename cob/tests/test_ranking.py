from django.test import TestCase, Client
from rest_framework.exceptions import ErrorDetail
from ..models import Competicao, Atleta, Resultado
from .base_api_test import BaseApiTest
from rest_framework import status


class RankingTestCase(BaseApiTest):
    # seta o endpoint
    path = '/ranking'

    def setUp(self):
        super().setUp()
        
        # cria competicoes
        self.corrida = Competicao.objects.create(
            nome='Cem Metros Final', condicao_para_vitoria='menor'
        )
        self.dardos = Competicao.objects.create(
            nome='Arremesso de Dardos Final', condicao_para_vitoria='maior_de_tres'
        )

        # Cria atletas
        self.fulano = Atleta.objects.create(nome='Fulano')
        self.ciclano = Atleta.objects.create(nome='Ciclano')
        self.beltrano = Atleta.objects.create(nome='Beltrano')

        # Criando registros de resultado
        Resultado.objects.create(competicao=self.corrida, atleta=self.fulano, resultado=12.134, unidade='s')
        Resultado.objects.create(competicao=self.corrida, atleta=self.ciclano, resultado=12.200, unidade='s')
        Resultado.objects.create(competicao=self.corrida, atleta=self.beltrano, resultado=10.321, unidade='s')
        # 1 tentativa
        Resultado.objects.create(competicao=self.dardos, atleta=self.fulano, resultado=52.300, unidade='m')
        Resultado.objects.create(competicao=self.dardos, atleta=self.ciclano, resultado=55.232, unidade='m')
        Resultado.objects.create(competicao=self.dardos, atleta=self.beltrano, resultado=44.354, unidade='m')
        # 2 tentativa
        Resultado.objects.create(competicao=self.dardos, atleta=self.fulano, resultado=70.02, unidade='m')
        Resultado.objects.create(competicao=self.dardos, atleta=self.ciclano, resultado=53.23, unidade='m')
        Resultado.objects.create(competicao=self.dardos, atleta=self.beltrano, resultado=50.12, unidade='m')
        # 3 tentativa
        Resultado.objects.create(competicao=self.dardos, atleta=self.fulano, resultado=66.14, unidade='m')
        Resultado.objects.create(competicao=self.dardos, atleta=self.ciclano, resultado=51.32, unidade='m')
        Resultado.objects.create(competicao=self.dardos, atleta=self.beltrano, resultado=52.24, unidade='m')

    def test_get_ranking_competicao_invalida(self):
        response = self.client.get(
            f'{self.path}/99999')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_ranking_ordena_corrida(self):
        response = self.client.get(f'{self.path}/1')

        resultado_menor = float(response.data[0]['resultado'])
        resultado_maior = float(response.data[1]['resultado'])

        self.assertEqual(response.data[0]['competicao'], 'Cem Metros Final')
        self.assertGreaterEqual(resultado_maior, resultado_menor)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_ranking_dardo(self):
        response = self.client.get(f'{self.path}/2')

        resultado_maior = float(response.data[0]['resultado'])
        resultado_menor = float(response.data[1]['resultado'])

        self.assertEqual(response.data[0]['competicao'], 'Arremesso de Dardos Final')
        self.assertGreaterEqual(resultado_maior, resultado_menor)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
