from rest_framework import serializers
from .models import negocio

class negocioSerializer(serializers.ModelSerializer):

    class Meta:
        model = negocio
        fields = ['nombre', 'ubicacion', 'tipo_negocio', 'descripcion']