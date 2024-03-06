from django.db import models


class Cargos(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200)


class Estados(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    sigla = models.CharField(max_length=2)


class Funcionarios(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200)
    idade = models.IntegerField
    email = models.EmailField
    celular = models.CharField(max_length=15)
    estado = models.CharField(max_length=30)
    cargo = models.ForeignKey(Cargos, on_delete=models.CASCADE)
    salario = models.FloatField


