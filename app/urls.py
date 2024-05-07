from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from staff.views import FuncionariosViewSet, CargosViewset, LinguagensViewSet, FuncionariosStatsViewSet, SenioridadeViewSet

router = routers.DefaultRouter()
router.register('funcionarios', FuncionariosViewSet, basename='funcionarios')
router.register('cargos', CargosViewset, basename='cargos')
router.register('linguagens', LinguagensViewSet, basename='linguagens')
router.register('senioridade', SenioridadeViewSet, basename='senioridade')
router.register('dados', FuncionariosStatsViewSet, basename='funcionarios-stats')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
