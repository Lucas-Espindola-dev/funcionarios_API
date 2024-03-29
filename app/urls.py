from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from staff.views import FuncionariosViewSet, CargosViewset, LinguagensViewSet, FuncionariosStats

router = routers.DefaultRouter()
router.register('funcionarios', FuncionariosViewSet, basename='funcionarios')
router.register('cargos', CargosViewset, basename='cargos')
router.register('linguagens', LinguagensViewSet, basename='linguagens')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('dados/', FuncionariosStats.as_view(), name='funcionarios-stats')
]
