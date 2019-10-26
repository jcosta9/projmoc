from django.db import models
from django.core.urlresolvers import reverse
from django.utils import timezone


class Bem(models.Model):
    nome = models.CharField(max_length=200)
    dataPreenchimento = models.DateField(default=timezone.now)
    codClassificacaoGeral = models.DecimalField(max_digits=8, decimal_places=0)
    preenchidoPor = models.ForeignKey('auth.User')

    def get_absolute_url(self):
        return reverse("bem_detail",kwargs={'pk':self.pk})

    def __str__(self):
        return self.nome
