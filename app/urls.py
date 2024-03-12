from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

router = routers.DefaultRouter()
router.register('funcionarios')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
