from django.db.models import Avg, Count
from staff.models import Funcionarios, Cargos, Linguagens
from staff.serializers import FuncionariosSerializer, CargosSerializer, LingugensSerializer
from rest_framework import viewsets, views, response, status


class FuncionariosViewSet(viewsets.ModelViewSet):
    queryset = Funcionarios.objects.all()
    serializer_class = FuncionariosSerializer


class CargosViewset(viewsets.ModelViewSet):
    queryset = Cargos.objects.all()
    serializer_class = CargosSerializer


class LinguagensViewSet(viewsets.ModelViewSet):
    queryset = Linguagens.objects.all()
    serializer_class = LingugensSerializer


class FuncionariosStats(views.APIView):
    queryset = Funcionarios.objects.all()

    def get(self, request):
        total_funcionarios = self.queryset.count()
        funcionarios_por_cargo = self.queryset.values('cargo__nome').annotate(count=Count('id'))
        funcionarios_por_linguagem = self.queryset.values('linguagem__nome').annotate(count=Count('id'))
        funcionarios_por_senioridade = self.queryset.values('senioridade__nome').annotate(count=Count('id'))
        media_salarial = self.queryset.values('linguagem__nome').annotate(media_sal=Avg('salario'))

        return response.Response(
            data={'Número de Funcionários': total_funcionarios,
                  'Funcionários por cargo': funcionarios_por_cargo,
                  'Funcionários por linguagem': funcionarios_por_linguagem,
                  'Media salarial por linguagem': media_salarial,
                  })
