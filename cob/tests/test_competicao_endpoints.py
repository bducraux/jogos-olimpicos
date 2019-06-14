from rest_framework import status
from django.urls import reverse
from ..models import Competicao
from ..serializers import CompeticaoSerializer
from .base_api_test import BaseApiTest
import json


class CompeticaoTest(BaseApiTest):

    # seta o endpoint
    path = "/competicao"

    def setUp(self):
        super().setUp()

        # cria competicoes
        self.competicao = Competicao.objects.create(
            nome="Dardos Eliminatoria Teste", condicao_para_vitoria="maior_de_tres"
        )
        self.competicao2 = Competicao.objects.create(
            nome="Cem Metros Teste", condicao_para_vitoria="menor"
        )

        # payload válido para create e update
        self.payload_valido = {
            'nome': 'Teste 1',
            'condicao_para_vitoria': 'menor',
            'status': 'aguardando'
        }

        # payload inválido para create e update
        self.payload_invalido = {
            'nome': '',
            'condicao_para_vitoria': 'menor',
            'status': 'aguardando'
        }

    def test_competicao_recuperar_todas(self):
        response = self.client.get(reverse('competicao-list'))

        competicoes = Competicao.objects.all()
        serializer = CompeticaoSerializer(competicoes, many=True)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_competicao_recuperar_uma_valida(self):
        response = self.client.get(
            reverse('competicao-detail', kwargs={'pk': self.competicao.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def est_competicao_recuperar_uma_invalida(self):
        response = self.client.get(
            reverse('competicao-detail', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_competicao_criacao_valida(self):
        response = self.client.post(
            reverse('competicao-list'),
            data=json.dumps(self.payload_valido),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_competicao_criacao_invalida(self):
        response = self.client.post(
            reverse('competicao-list'),
            data=json.dumps(self.payload_invalido),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_competicao_update_valido(self):
        response = self.client.put(
            reverse('competicao-detail', kwargs={'pk': self.competicao.pk}),
            data=json.dumps(self.payload_valido),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_competicao_update_invalido(self):
        response = self.client.put(
            reverse('competicao-detail', kwargs={'pk': self.competicao.pk}),
            data=json.dumps(self.payload_invalido),
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_competicao_patch_valido(self):
        payload = {
            'status': 'encerrada'
        }

        response = self.client.patch(
            reverse('competicao-detail', kwargs={'pk': self.competicao.pk}),
            data=json.dumps(payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_competicao_patch_invalido(self):
        payload = {
            'status': 'encerrada'
        }

        response = self.client.patch(
            reverse('competicao-detail', kwargs={'pk': 30}),
            data=json.dumps(payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_competicao_patch_status_invalido(self):
        payload = {
            'status': 'encerradaaaaa'
        }
        response = self.client.patch(
            reverse('competicao-detail', kwargs={'pk': self.competicao.pk}),
            data=json.dumps(payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_competicao_patch_condicao_para_vitoria_invalido(self):
        payload = {
            'condicao_para_vitoria': 'aaa'
        }
        response = self.client.patch(
            reverse('competicao-detail', kwargs={'pk': self.competicao.pk}),
            data=json.dumps(payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_competicao_delete_valido(self):
        response = self.client.delete(
            reverse('competicao-detail', kwargs={'pk': self.competicao.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_competicao_delete_invalido(self):
        response = self.client.delete(
            reverse('competicao-detail', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
