from django.db import models


class BaseModel:
    """
    Adiciona metodos comuns a todos os módulos
    """
    @classmethod
    def recuperar_registro_pelo_id(cls, id):
        """
        Retorna o objeto relacionado ao id passado

        :return: objeto relacionado ao id
        """
        try:
            return cls.objects.get(pk=id)
        except cls.DoesNotExist:
            return False


class Competicao(models.Model, BaseModel):

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

    nome = models.CharField("Nome da competição", max_length=100)
    condicao_para_vitoria = models.CharField("Condição para vitória", max_length=13, choices=CONDICAO_PARA_VITORIA)
    status = models.CharField("Status da competição", max_length=10, choices=STATUS, default='aguardando')

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "competição"
        verbose_name_plural = "competições"
        ordering = ('id',)


class Atleta(models.Model):

    nome = models.CharField("Nome do atleta", max_length=200)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ('nome',)


class Resultado(models.Model):

    competicao = models.ForeignKey(Competicao, on_delete=models.CASCADE)
    atleta = models.ForeignKey(Atleta, on_delete=models.CASCADE)
    resultado = models.DecimalField("Valor do resultado obtido pelo atleta", max_digits=8, decimal_places=3)

    def __str__(self):
        return "%s - %s - %s" % (self.competicao, self.atleta, self.resultado)

    class Meta:
        ordering = ('id',)
