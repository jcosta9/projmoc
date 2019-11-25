import qrcode
from io import StringIO
from django.core.files import File

from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.core.files.uploadedfile import InMemoryUploadedFile

# definicoes
ESTADO_NOVO = 1
ESTADO_USADO = 2
ESTADO_MBOM = 3
ESTADO_BOM = 4
ESTADO_MAU = 5

ESTADOS_BEM = (
    (ESTADO_NOVO, ('Novo')),
    (ESTADO_USADO, ('Usado')),
    (ESTADO_MBOM, ('Muito Bom')),
    (ESTADO_BOM, ('Bom')),
    (ESTADO_MAU, ('Mau')),
)

SIM = 1
NAO = 2

QRCODE_LOC = 'media/qrcodes/'


class Uge(models.Model):
    # TODO: atrelar a designacoes
    # TODO: criar lista suspensa
    cod = models.DecimalField(max_digits=8, decimal_places=0, primary_key=True)
    designacoes = models.CharField(max_length=256)

    def get_absolute_url(self):
        return reverse("gest_patr:uge_detalhe",kwargs={'pk':self.pk})

    def __str__(self):
        return self.designacoes

class Ugb(models.Model):
    cod = models.DecimalField(max_digits=8, decimal_places=0, primary_key=True)
    designacoes = models.CharField(max_length=256)

    def get_absolute_url(self):
        return reverse("gest_patr:ugb_detalhe",kwargs={'pk':self.pk})

    def __str__(self):
        return self.designacoes

class Sector(models.Model):
    cod = models.DecimalField(max_digits=8, decimal_places=0, primary_key=True)
    nome = models.CharField(max_length=256)
    uge = models.ForeignKey('Uge',on_delete=models.CASCADE,default='21010000')
    ugb = models.ForeignKey('Ugb',on_delete=models.CASCADE,default='21030000')
    provincia = models.CharField(max_length=256)
    distrito = models.CharField(max_length=256)
    postAdmin = models.CharField(max_length=256)
    localidade = models.CharField(max_length=256)
    classificadorTerr = models.DecimalField(max_digits=6, decimal_places=0)
    bairro = models.CharField(max_length=256)
    endereco = models.CharField(max_length=256)

    def get_absolute_url(self):
        return reverse("gest_patr:sector_detalhe",kwargs={'pk':self.pk})

    def __str__(self):
        return self.nome

class Fornecedor(models.Model):
    nome = models.CharField(max_length=256)
    nuit = models.DecimalField(max_digits=12, decimal_places=0)
    enderecoFornecedor = models.CharField(max_length=256)
    cidade = models.CharField(max_length=256)

    def get_absolute_url(self):
        return reverse("gest_patr:fornecedor_detalhe",kwargs={'pk':self.pk})

    def __str__(self):
        return self.nome

class Bem(models.Model):

    # seção 1 - entidade/localizacao institucional e geografica
    numOrdem = models.DecimalField(max_digits=8, decimal_places=0, null=True) #, primary_key=True)
    nome = models.CharField(max_length=200)
    dataPreenchimento = models.DateField(default=timezone.now)

    uge = models.ForeignKey('Uge', on_delete=models.CASCADE, default='21010000')
    ugb = models.ForeignKey('Ugb', on_delete=models.CASCADE, default='21030000')
    sector = models.ForeignKey('Sector', on_delete=models.CASCADE, default='001')

    # seção 2 - identificacao e caracterizacao
    codClassificacaoGeral = models.DecimalField(max_digits=8, decimal_places=0,null=True)
    designacao = models.CharField(max_length=256,null=True)
    marca = models.CharField(max_length=256,null=True)
    numeroSerie = models.CharField(max_length=256,null=True)
    NIP = models.DecimalField(max_digits=10, decimal_places=0, null=True)
    modelo = models.CharField(max_length=256,null=True)
    comprimento = models.SmallIntegerField(null=True)
    largura = models.SmallIntegerField(null=True)
    altura = models.SmallIntegerField(null=True)
    cor = models.CharField(max_length=256,null=True)
    materialPredominante = models.CharField(max_length=256,null=True)

    estadoBem = models.PositiveSmallIntegerField(
        choices=ESTADOS_BEM,
        default=ESTADO_BOM
    )
    tipoAquisicao = models.PositiveSmallIntegerField(
        choices=(
            (0, ('Compra')),
            (1, ('Transferência')),
            (2, ('Doação'))
        ),
        default=0
    )
    dataAquisicao = models.DateField(null=True)
    valor = models.IntegerField(null=True)

    # secao 3 - outras informacoes
    fornecedor = models.ForeignKey('Fornecedor', on_delete=models.CASCADE, null=True)
    tipoComprovativo = models.CharField(max_length=256,null=True)
    nroComprovativo = models.DecimalField(max_digits=10, decimal_places=0,null=True)
    assistenciaTecnica = models.PositiveSmallIntegerField(
        choices=(
            (SIM, ('Sim')),
            (NAO, ('Nao')),
        ),
        default=NAO
    )
    garantia = models.CharField(max_length=256,null=True)
    utilizador = models.CharField(max_length=256,null=True)
    observacoes = models.TextField(null=True)
    # preenchidoPor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    preenchidoPor = models.CharField(max_length=256,null=True)
    responsavel = models.CharField(max_length=256,null=True)
    qrcode = models.ImageField(upload_to='qrcodes/', blank=True, null=True)

    def get_absolute_url(self):
        return reverse("gest_patr:bem_detalhe",kwargs={'pk':self.pk})

    def __str__(self):
        return self.nome

    def save(self):
        super(Bem, self).save()
        self.generate_qrcode()
        self.qrcode = 'qrcodes/bem-%s.png' % (self.id)
        super(Bem, self).save()

    def generate_qrcode(self):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=6,
            border=0,
        )
        qr.add_data(self.get_absolute_url())
        qr.make(fit=True)
        img = qr.make_image()
        img.save(QRCODE_LOC+'bem-%s.png' % (self.id))
