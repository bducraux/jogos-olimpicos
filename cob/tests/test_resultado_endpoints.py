from rest_framework import status
from django.urls import reverse
from ..models import Competicao, Atleta, Resultado
from ..serializers import ResultadoSerializer
from .base_api_test import BaseApiTest
import json


class ResultadoTest(BaseApiTest):

    # seta o endpoint
    path = "/atleta"

    def setUp(self):
        super().setUp()

        # cria competicao
        self.competicao = Competicao.objects.create(
            nome="Dardos Eliminatoria Teste", condicao_para_vitoria="maior_de_tres"
        )
        # cria atleta
        self.atleta = Atleta.objects.create(
            nome="Teste"
        )
        
        # cria resultados
        self.resultado1 = Resultado.objects.create(competicao=self.competicao, atleta=self.atleta, resultado='20.140')
        self.resultado2 = Resultado.objects.create(competicao=self.competicao, atleta=self.atleta, resultado='22.11')

        # payload válido para create e update
        self.payload_valido = {
            'competicao': self.competicao.id,
            'atleta': self.atleta.id,
            'resultado': '27.02'
        }

        # payload inválido para create e update
        self.payload_invalido = {
            'competicao': '',
            'atleta': self.atleta.id,
            'resultado': '27.02'
        }

    def test_resultado_recuperar_todas(self):
        response = self.client.get(reverse('resultado-list'))

        resultados = Resultado.objects.all()
        serializer = ResultadoSerializer(resultados, many=True)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_resultado_recuperar_uma_valida(self):
        response = self.client.get(
            reverse('resultado-detail', kwargs={'pk': self.resultado1.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def est_resultado_recuperar_uma_invalida(self):
        response = self.client.get(
            reverse('resultado-detail', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_resultado_criacao_valida(self):
        response = self.client.post(
            reverse('resultado-list'),
            data=json.dumps(self.payload_valido),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_resultado_criacao_invalida(self):
        response = self.client.post(
            reverse('resultado-list'),
            data=json.dumps(self.payload_invalido),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_resultado_update_valido(self):
        response = self.client.put(
            reverse('resultado-detail', kwargs={'pk': self.resultado1.pk}),
            data=json.dumps(self.payload_valido),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_resultado_update_invalido(self):
        response = self.client.put(
            reverse('resultado-detail', kwargs={'pk': self.resultado1.pk}),
            data=json.dumps(self.payload_invalido),
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_resultado_patch_valido(self):
        payload = {
            'nome': 'Teste 3'
        }

        response = self.client.patch(
            reverse('resultado-detail', kwargs={'pk': self.resultado1.pk}),
            data=json.dumps(payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_resultado_patch_invalido(self):
        payload = {
            'nome': 'Teste 3'
        }

        response = self.client.patch(
            reverse('resultado-detail', kwargs={'pk': 30}),
            data=json.dumps(payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_resultado_delete_valido(self):
        response = self.client.delete(
            reverse('resultado-detail', kwargs={'pk': self.resultado1.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_resultado_delete_invalido(self):
        response = self.client.delete(
            reverse('resultado-detail', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
