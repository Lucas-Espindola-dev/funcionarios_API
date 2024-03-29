from django.db import models


class Cargos(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome


class Estados(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    sigla = models.CharField(max_length=2)

    def __str__(self):
        return self.name


class Linguagens(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome


class Funcionarios(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200)
    idade = models.IntegerField()
    email = models.CharField(max_length=250)
    celular = models.CharField(max_length=15)
    estado = models.ForeignKey(Estados, on_delete=models.PROTECT, related_name='estado')
    cargo = models.ManyToManyField(Cargos, related_name='cargos')
    salario = models.FloatField()
    linguagem = models.ManyToManyField(Linguagens, related_name='linguagem')



