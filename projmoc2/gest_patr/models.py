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

class Bem(models.Model):
    nome = models.CharField(max_length=200)
    dataPreenchimento = models.DateField(default=timezone.now)
    marca = models.CharField(max_length=256)
    valor = models.IntegerField()
    uge = models.ForeignKey('Uge', on_delete=models.CASCADE, default='21010000')
    ugb = models.ForeignKey('Ugb', on_delete=models.CASCADE, default='21030000')
    # preenchidoPor = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("gest_patr:bem_detalhe",kwargs={'pk':self.pk})

    def __str__(self):
        return self.nome
