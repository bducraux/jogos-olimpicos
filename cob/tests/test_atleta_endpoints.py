from rest_framework import status
from django.urls import reverse
from ..models import Atleta
from ..serializers import AtletaSerializer
from .base_api_test import BaseApiTest
import json


class AtletaTest(BaseApiTest):

    # seta o endpoint
    path = "/atletao"

    def setUp(self):
        super().setUp()

        # cria atletas
        self.atleta = Atleta.objects.create(
            nome="Teste"
        )
        self.atleta2 = Atleta.objects.create(
            nome="Teste 2"
        )

        # payload válido para create e update
        self.payload_valido = {
            'nome': 'Teste 1'
        }

        # payload inválido para create e update
        self.payload_invalido = {
            'nome': ''
        }

    def test_atleta_recuperar_todas(self):
        response = self.client.get(reverse('atleta-list'))

        atletas = Atleta.objects.all()
        serializer = AtletaSerializer(atletas, many=True)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_atleta_recuperar_uma_valida(self):
        response = self.client.get(
            reverse('atleta-detail', kwargs={'pk': self.atleta.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def est_atleta_recuperar_uma_invalida(self):
        response = self.client.get(
            reverse('atleta-detail', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_atleta_criacao_valida(self):
        response = self.client.post(
            reverse('atleta-list'),
            data=json.dumps(self.payload_valido),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_atleta_criacao_invalida(self):
        response = self.client.post(
            reverse('atleta-list'),
            data=json.dumps(self.payload_invalido),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_atleta_update_valido(self):
        response = self.client.put(
            reverse('atleta-detail', kwargs={'pk': self.atleta.pk}),
            data=json.dumps(self.payload_valido),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_atleta_update_invalido(self):
        response = self.client.put(
            reverse('atleta-detail', kwargs={'pk': self.atleta.id}),
            data=json.dumps(self.payload_invalido),
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_atleta_patch_valido(self):
        payload = {
            'nome': 'Teste 3'
        }

        response = self.client.patch(
            reverse('atleta-detail', kwargs={'pk': self.atleta.pk}),
            data=json.dumps(payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_atleta_patch_invalido(self):
        payload = {
            'nome': 'Teste 3'
        }

        response = self.client.patch(
            reverse('atleta-detail', kwargs={'pk': 30}),
            data=json.dumps(payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_atleta_delete_valido(self):
        response = self.client.delete(
            reverse('atleta-detail', kwargs={'pk': self.atleta.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_atleta_delete_invalido(self):
        response = self.client.delete(
            reverse('atleta-detail', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
