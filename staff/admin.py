from django.contrib import admin
from staff.models import Funcionarios, Cargos, Estados


class FuncionariosAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cargo', 'idade', 'salario')
    search_fields = ('nome', 'cargo',)


admin.site.register(Funcionarios, FuncionariosAdmin)


class CargosAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')


admin.site.register(Cargos, CargosAdmin)
