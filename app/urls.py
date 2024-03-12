from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from staff.views import FuncionariosViewSet

router = routers.DefaultRouter()
router.register('funcionarios', FuncionariosViewSet, basename='funcionarios')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
