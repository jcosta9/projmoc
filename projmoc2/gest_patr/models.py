from django.db import models
from django.urls import reverse
from django.utils import timezone

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

class Bem(models.Model):
    nome = models.CharField(max_length=200)
    dataPreenchimento = models.DateField(default=timezone.now)
    marca = models.CharField(max_length=256)
    valor = models.IntegerField()
    uge = models.ForeignKey('Uge', on_delete=models.CASCADE, default='21010000')
    ugb = models.ForeignKey('Ugb', on_delete=models.CASCADE, default='21030000')
    sector = models.ForeignKey('Sector', on_delete=models.CASCADE, default='001')
    # preenchidoPor = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("gest_patr:bem_detalhe",kwargs={'pk':self.pk})

    def __str__(self):
        return self.nome
