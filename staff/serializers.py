from rest_framework import serializers
from staff.models import Funcionarios, Linguagens, Cargos, Senioridade


class LingugensSerializer(serializers.ModelSerializer):
    class Meta:
        model = Linguagens
        fields = '__all__'


class CargosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cargos
        fields = '__all__'


class SenioridadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Senioridade
        fields = '__all__'


class FuncionariosModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcionarios
        fields = '__all__'


class FuncionariosListDetailSerializer(serializers.ModelSerializer):
    cargo = CargosSerializer()
    linguagem = LingugensSerializer(many=True)
    senioridade = SenioridadeSerializer()

    class Meta:
        model = Funcionarios
        fields = ['id', 'nome', 'cargo', 'linguagem', 'senioridade',
                  'salario', 'idade', 'email', 'celular', 'estado', ]
