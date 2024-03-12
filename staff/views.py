from staff.models import Funcionarios, Cargos
from staff.serializers import FuncionariosSerializer, CargosSerializer
from rest_framework import viewsets


class FuncionariosViewSet(viewsets.ModelViewSet):
    queryset = Funcionarios.objects.all()
    serializer_class = FuncionariosSerializer


class CargosViewset(viewsets.ModelViewSet):
    queryset = Cargos.objects.all()
    serializer_class = CargosSerializer
