from django.db import models
from django.utils.translation import gettext as _

ESTADO_NOVO = 1
ESTADO_USADO = 2
ESTADO_MBOM = 3
ESTADO_BOM = 4
ESTADO_MAU = 5

ESTADOS_BEM = (
    (ESTADO_NOVO, _('Novo')),
    (ESTADO_USADO, _('Usado')),
    (ESTADO_MBOM, _('Muito Bom')),
    (ESTADO_BOM, _('Bom')),
    (ESTADO_MAU, _('Mau')),
)

SIM = 1
NAO = 2


# Create your models here.

class Uge(models.Model):
    # TODO: atrelar a designacoes
    # TODO: criar lista suspensa
    cod = models.DecimalField(max_digits=8, decimal_places=0, primary_key=True)
    designacoes = models.CharField(max_length=256)

class Ugb(models.Model):
    cod = models.DecimalField(max_digits=8, decimal_places=0, primary_key=True)
    designacoes = models.CharField(max_length=256)

class Sector(models.Model):
    cod = models.DecimalField(max_digits=8, decimal_places=0, primary_key=True)
    nome = models.CharField(max_length=256)
    ugb = models.ForeignKey('Ugb',on_delete=models.CASCADE,)
    provincia = models.CharField(max_length=256)
    distrito = models.CharField(max_length=256)
    postAdmin = models.CharField(max_length=256)
    localidade = models.CharField(max_length=256)
    classificadorTerr = models.DecimalField(max_digits=6, decimal_places=0)
    bairro = models.CharField(max_length=256)
    endereco = models.CharField(max_length=256)

class Aquisicao(models.Model):
    cod = models.DecimalField(max_digits=10, decimal_places=0, primary_key=True)
    forma = models.CharField(max_length=256)

class Fornecedor(models.Model):
    nome = models.CharField(max_length=256)
    nuit = models.DecimalField(max_digits=12, decimal_places=0)
    enderecoFornecedor = models.CharField(max_length=256)
    cidade = models.CharField(max_length=256)

class BemMovel(models.Model):
    # seção 1 - entidade/localizacao institucional e geografica
    numOrdem = models.DecimalField(max_digits=8, decimal_places=0, primary_key=True)
    dataPreenchimento = models.DateField()

    uge = models.ForeignKey('Uge',on_delete=models.CASCADE,)
    ugb = models.ForeignKey('Ugb',on_delete=models.CASCADE,)
    sector = models.ForeignKey('Sector',on_delete=models.CASCADE,)

    # seção 2 - identificacao e caracterizacao
    codClassificacaoGeral = models.DecimalField(max_digits=8, decimal_places=0)
    designacao = models.CharField(max_length=256)
    marca = models.CharField(max_length=256)
    numeroSerie = models.CharField(max_length=256)
    NIP = models.DecimalField(max_digits=10, decimal_places=0)
    modelo = models.CharField(max_length=256)
    comprimento = models.SmallIntegerField()
    largura = models.SmallIntegerField()
    altura = models.SmallIntegerField()
    cor = models.CharField(max_length=256)
    materialPredominante = models.CharField(max_length=256)

    models.ForeignKey('Aquisicao',on_delete=models.CASCADE,)

    estadoBem = models.PositiveSmallIntegerField(
        choices=ESTADOS_BEM,
        default=ESTADO_BOM
    )
    dataAquisicao = models.DateField()
    valorAquisicao = models.IntegerField()

    # secao 3 - outras informacoes
    fornecedor = models.ForeignKey('Fornecedor',on_delete=models.CASCADE,)
    tipoComprovativo = models.CharField(max_length=256)
    nroComprovativo = models.DecimalField(max_digits=10, decimal_places=0)
    assistenciaTecnica = models.PositiveSmallIntegerField(
        choices=(
            (SIM, _('Sim')),
            (NAO, _('Nao')),
        ),
        default=NAO
    )
    garantia = models.CharField(max_length=256)
    utilizador = models.CharField(max_length=256)
    observacoes = models.CharField(max_length=2048)
    preenchidoPor = models.CharField(max_length=256)
    responsavel = models.CharField(max_length=256)

# class MyForm(forms.ModelForm):
#     prioritylevel = forms.ModelChoiceField(queryset=OtherModel.objects.values('level'))
