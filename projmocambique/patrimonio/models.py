from django.db import models

# Create your models here.
class User(models.Model):
    #entender melhor as regras do negócio para a criação de usuários
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.EmailField(max_length=254,unique=True)
