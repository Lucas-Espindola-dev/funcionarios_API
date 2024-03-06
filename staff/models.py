from django.db import models


class Funcionarios(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200)
    idade = models.CharField(max_length=15)
    email = models.EmailField
    cargo = models.CharField(max_length=200)
    salario = models.FloatField


