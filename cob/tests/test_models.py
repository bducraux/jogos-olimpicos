from django.test import TestCase
from ..models import Competicao, Atleta, Resultado


class ModelsTest(TestCase):

    def SetUp(self):
        pass

    # Testa pegar uma competição passando o id
    def test_recupera_registro_pelo_id(self):
        # cria uma competição
        Competicao.objects.create(
            nome="Dardos Eliminatoria Teste", condicao_para_vitoria="maior_de_tres")

        expected = "Dardos Eliminatoria Teste"

        competicao = Competicao().recuperar_registro_pelo_id(1)

        self.assertEqual(expected, competicao.nome)

    def test_recuperar_por_id(selfs):
        # competicao_obj = Competicao.objects.get(pk=1)
        pass
