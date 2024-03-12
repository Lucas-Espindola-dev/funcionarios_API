from rest_framework import serializers
from staff.models import Funcionarios, Linguagens, Cargos


class FuncionariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcionarios
        fields = '__all__'


class LingugensSerializer(serializers.ModelSerializer):
    class Meta:
        model = Linguagens
        fields = '__all__'
