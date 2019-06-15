from django.test import TestCase
from ..models import Competicao, Atleta, Resultado


class CompeticaoTest(TestCase):

    def setUp(self):
        # cria a competição
        self.c_dardos = Competicao.objects.create(
            nome='Dardos Eliminatoria Teste', condicao_para_vitoria='maior_de_tres'
        )
        self.c_corrida = Competicao.objects.create(
            nome='Cem Metros Rasos Eliminatoria Teste', condicao_para_vitoria='menor'
        )

        # cria Atleta
        self.a = Atleta.objects.create(nome='Teste')

        # cria resultado
        self.resultado = Resultado.objects.create(
            competicao=self.c_dardos,
            atleta=self.a,
            resultado='20.12',
            unidade='m'
        )

    def test_competicao_criacao_dardos(self):
        # recupera a competicao de dardos criada
        competicao = Competicao.objects.get(id=self.c_dardos.id)

        expected_object_name = f'{competicao.__str__()}'

        self.assertEquals(expected_object_name, 'Dardos Eliminatoria Teste')
        self.assertTrue(isinstance(competicao, Competicao))

    def test_competicao_criacao_corrida(self):
        # recupera a competicao de corrida criada
        competicao = Competicao.objects.get(id=self.c_corrida.id)

        expected_object_name = f'{competicao.__str__()}'

        self.assertEquals(expected_object_name, 'Cem Metros Rasos Eliminatoria Teste')
        self.assertTrue(isinstance(competicao, Competicao))

    def test_atleta_criacao(self):
        # recupera o atleta criado
        atleta = Atleta.objects.get(id=1)

        expected_object_name = f'{atleta.__str__()}'

        self.assertEquals(expected_object_name, 'Teste')
        self.assertTrue(isinstance(atleta, Atleta))

    def test_resultado_criacao_dardos(self):
        # recupera o resultado criado
        resultado = Resultado.objects.get(id=1)

        expected_object_name = f'{resultado.__str__()}'

        self.assertEquals(expected_object_name, 'Dardos Eliminatoria Teste - Teste - 20.120 m')
        self.assertTrue(isinstance(resultado, Resultado))

    def test_resultado_tentativas_increment(self):
        # cria resultado
        resultado1 = Resultado.objects.create(
            competicao=self.c_dardos,
            atleta=self.a,
            resultado='20.12',
            unidade='m'
        )
        resultado2 = Resultado.objects.create(
            competicao=self.c_dardos,
            atleta=self.a,
            resultado='25.12',
            unidade='m'
        )
