from django.contrib import admin
from staff.models import Funcionarios, Cargos, Estados


class FuncionariosAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cargo', 'email', 'estado',)
    search_fields = ('nome', 'cargo',)
