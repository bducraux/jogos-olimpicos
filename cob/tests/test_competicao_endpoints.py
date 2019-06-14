from rest_framework import status
from django.urls import reverse
from ..models import Competicao
from ..serializers import CompeticaoSerializer
from .base_api_test import BaseApiTest


class CompeticaoTest(BaseApiTest):

    # seta o endpoint
    path = "/competicao"

    def setUp(self):
        super().setUp()

        # cria competicoes
        self.dardos_eliminatoria = Competicao.objects.create(
            nome="Dardos Eliminatoria Teste",condicao_para_vitoria="maior_de_tres")
        self.cem_metros_eliminatoria = Competicao.objects.create(
            nome="100 metros Eliminatoria Teste", condicao_para_vitoria="menor")
        self.dardos_final = Competicao.objects.create(
            nome="Dardos Final Teste", condicao_para_vitoria="maior_de_tres")
        self.cem_metros_final = Competicao.objects.create(
            nome="100 metros Final Teste", condicao_para_vitoria="menor")

    # TESTES DO MÓDULO



    # TESTES DA API

    def test_competicao_endpoint_list(self):
        """
        Esse teste garante que todas as competicoes adicionadas mo método setUp
        existem quando fizermos um GET request para  competicao/ endpoint
        """

        response = self.client.get(reverse('competicao-list'))

        expected = Competicao.objects.all()

        serialized = CompeticaoSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_competicao_endpoint_por_id(self):
        """
        Esse teste garante que a competicao adicionada mo método setUp
        existe quando fizermos um GET request para  competicao/1 endpoint
        """

        response = self.client.get(reverse('competicao-detail', kwargs={'pk': 1}))

        expected = Competicao.recuperar_registro_pelo_id(1)

        serialized = CompeticaoSerializer(expected)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
