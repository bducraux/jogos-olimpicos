from django.test import TestCase
from ..models import Competicao, Atleta, Resultado


class CompeticaoTest(TestCase):

    def setUp(self):
        # cria a competição
        c = Competicao.objects.create(
            nome='Dardos Eliminatoria Teste', condicao_para_vitoria='maior_de_tres'
        )

        # cria Atleta
        a = Atleta.objects.create(nome='Teste')

        # cria resultado
        Resultado.objects.create(
            competicao=c,
            atleta=a,
            resultado='20.12'
        )

    def test_competicao_criacao(self):
        # recupera a competicao criada
        competicao = Competicao.objects.get(id=1)

        expected_object_name = f'{competicao.__str__()}'

        self.assertEquals(expected_object_name, 'Dardos Eliminatoria Teste')
        self.assertTrue(isinstance(competicao, Competicao))

    def test_atleta_criacao(self):
        # recupera o atleta criado
        atleta = Atleta.objects.get(id=1)

        expected_object_name = f'{atleta.__str__()}'

        self.assertEquals(expected_object_name, 'Teste')
        self.assertTrue(isinstance(atleta, Atleta))

    def test_resultado_criacao(self):
        # recupera o resultado criado
        resultado = Resultado.objects.get(id=1)

        expected_object_name = f'{resultado.__str__()}'

        self.assertEquals(expected_object_name, 'Dardos Eliminatoria Teste - Teste - 20.120')
        self.assertTrue(isinstance(resultado, Resultado))
