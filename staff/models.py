from django.db import models


class Funcionarios(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200)
    idade = models.IntegerField
    email = models.EmailField
    celular = models.CharField(max_length=15)
    estado = models.CharField(max_length=30)
    cargo = models.CharField(max_length=200)
    salario = models.FloatField

