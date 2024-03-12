from django.shortcuts import render
from staff.models import Funcionarios
from staff.serializers import FuncionariosSerializer
from rest_framework import viewsets


class FuncionariosViewSet(viewsets.ModelViewSet):
    queryset = Funcionarios.objects.all()
    serializer_class = FuncionariosSerializer
