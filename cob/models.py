from django.db import models
from rest_framework.exceptions import ValidationError
from django.shortcuts import get_object_or_404


class Competicao(models.Model):

    STATUS = (
        ('aguardando', 'Aguardando início'),
        ('competindo', 'Competição em andamento'),
        ('encerrada', 'Competição Encerrada'),
    )

    CONDICAO_PARA_VITORIA = (
        ('maior', 'Maior_resultado vence'),
        ('menor', 'Menor resultado vence'),
        ('maior_de_tres', 'Maior de três resultados vence'),
        ('menor_de_tres', 'Menor de três resultados vence'),
    )

    nome = models.CharField('Nome da competição', max_length=100)
    condicao_para_vitoria = models.CharField('Condição para vitória', max_length=13, choices=CONDICAO_PARA_VITORIA)
    status = models.CharField('Status da competição', max_length=10, choices=STATUS, default='aguardando')

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'competição'
        verbose_name_plural = 'competições'
        ordering = ('id',)


class Atleta(models.Model):

    nome = models.CharField('Nome do atleta', max_length=200, unique=True)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ('nome',)


class Resultado(models.Model):
    UNIDADE = (
        ('m', 'Metros'),
        ('s', 'Segundos'),
    )

    tentativas_maximas = 3

    competicao = models.ForeignKey(Competicao, on_delete=models.CASCADE)
    atleta = models.ForeignKey(Atleta, on_delete=models.CASCADE)
    resultado = models.DecimalField('Valor do resultado obtido pelo atleta', max_digits=8, decimal_places=3)
    unidade = models.CharField(max_length=13, choices=UNIDADE)
    tentativa = models.IntegerField(default=1)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        # ultimo resultado
        ultimo_resultado = Resultado.objects.filter(
            atleta_id=self.atleta.id,
            competicao_id=self.competicao.id
            ).last()

        if ultimo_resultado:
            self.tentativa = ultimo_resultado.tentativa +1

        # caso ultrapasse o número max de tantativa impede a gravação no banco e gera um response informando o erro
        if self.tentativa > self.tentativas_maximas:
            raise ValidationError(detail='Só são permitidas 3 tentativas por atleta.')

        # impede a gravação caso a competicao esteja encerrada
        if self.competicao.status == 'encerrada':
            raise ValidationError(detail='Não é possívem cadastrar resuldados, pois a competição já encerrou.')

        # grava o registro no banco
        super(Resultado, self).save()

    @staticmethod
    def _filtrar_melhor_resultado(resultados):
        ranking = []
        atletas = []
        for result in resultados:
            atleta = result.atleta_id
            if atleta not in atletas:
                atletas.append(atleta)
                ranking.append(result)

        return ranking

    @classmethod
    def pegar_rank_da_competicao(cls, id_competicao):
        """
        Retorna os resultados rankeados de uma competição
        de acordo com a condição para vitória da competição
        """

        competicao = get_object_or_404(Competicao, id=id_competicao)

        # seta a ordenacao de acordo com a condicao para vitoria
        if competicao.condicao_para_vitoria in ('menor', 'menor_de_tres'):
            order_by = r'resultado'
        else:
            order_by = r'-resultado'

        resultados = Resultado.objects.filter(competicao=competicao.id).order_by(order_by)
        return cls._filtrar_melhor_resultado(resultados)

    def __str__(self):
        _str = '%s - %s - %s %s' % (self.competicao, self.atleta, self.resultado, self.unidade)
        return _str

    class Meta:
        ordering = ('id',)
