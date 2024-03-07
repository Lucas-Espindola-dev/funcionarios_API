from rest_framework import serializers
from staff.models import Funcionarios


class FuncionariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcionarios
        fields = '__all__'

