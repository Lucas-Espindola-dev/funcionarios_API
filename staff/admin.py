from django.contrib import admin
from staff.models import Funcionarios, Cargos, Estados


class FuncionariosAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cargo', 'idade', 'email', 'estado', 'salario', 'celular')
    search_fields = ('nome', 'cargo',)


admin.site.register(Funcionarios, FuncionariosAdmin)
