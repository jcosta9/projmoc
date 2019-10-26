from django.db import models
from django.urls import reverse
from django.utils import timezone


class Bem(models.Model):
    nome = models.CharField(max_length=200)
    dataPreenchimento = models.DateField(default=timezone.now)
    marca = models.CharField(max_length=256)
    valor = models.IntegerField()
    # preenchidoPor = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("gest_patr:bem_detalhe",kwargs={'pk':self.pk})

    def __str__(self):
        return self.nome
