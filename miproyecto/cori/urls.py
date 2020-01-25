
from django.urls import path
from .views import home
from .views import registro_usuario

urlpatterns = [
    path('', home, name="home"),
    path('registro/', registro_usuario, name='registro_usuario'),
]