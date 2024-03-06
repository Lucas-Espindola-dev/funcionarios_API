from django.db import models


class Cargos(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200)


class Estados(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    sigla = models.CharField(max_length=2)


class Linguagens(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200)


class Funcionarios(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200)
    idade = models.IntegerField()
    email = models.CharField(max_length=250)
    celular = models.CharField(max_length=15)
    estado = models.ForeignKey(Estados, on_delete=models.PROTECT)
    cargo = models.ManyToManyField(Cargos)
    salario = models.FloatField()
    linguagem = models.ManyToManyField(Linguagens, limit_choices_to=5)



