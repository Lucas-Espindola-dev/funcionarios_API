from django.contrib import admin
from staff.models import Funcionarios, Cargos, Estados, Linguagens


class FuncionariosAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'idade', 'salario')
    search_fields = ('nome', 'cargo',)


admin.site.register(Funcionarios, FuncionariosAdmin)


class CargosAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')


admin.site.register(Cargos, CargosAdmin)


class EstadosAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'sigla')


admin.site.register(Estados, EstadosAdmin)


class LinguagensAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')


admin.site.register(Linguagens, LinguagensAdmin)
