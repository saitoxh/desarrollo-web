
from django.urls import path, include
from .views import home, mis_negocios, nuevo_negocio, modificar_negocio, eliminar_negocio, negocioViewSet, guardar_token
from .views import registro_usuario
from rest_framework import routers

router = routers.DefaultRouter()
router.register('negocio', negocioViewSet)

urlpatterns = [
    path('', home, name="home"),
    path('registro/', registro_usuario, name='registro_usuario'),
    path('mis_negocios/', mis_negocios, name="mis negocios"),
    path('nuevo_negocio/', nuevo_negocio, name="nuevo negocio"),
    path('modificar_negocio/<id>/', modificar_negocio, name="modificar negocio"),
    path('eliminar_negocio/<id>/', eliminar_negocio, name="eliminar negocio"),
    path('api/', include(router.urls)),
    path('guardar_token/',guardar_token, name='guardar_token' ),
]