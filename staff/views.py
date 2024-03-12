from staff.models import Funcionarios, Cargos, Linguagens
from staff.serializers import FuncionariosSerializer, CargosSerializer, LingugensSerializer
from rest_framework import viewsets


class FuncionariosViewSet(viewsets.ModelViewSet):
    queryset = Funcionarios.objects.all()
    serializer_class = FuncionariosSerializer


class CargosViewset(viewsets.ModelViewSet):
    queryset = Cargos.objects.all()
    serializer_class = CargosSerializer


class LinguagensViewSet(viewsets.ModelViewSet):
    queryset = Linguagens.objects.all()
    serializer_class = LingugensSerializer
