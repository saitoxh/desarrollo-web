from django.contrib import admin
from .models import tipo_negocio, negocio
# Register your models here.

class negociosAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'ubicacion', 'tipo_negocio']
    search_fields = ['nombre', 'ubicacion']
    list_filter = ['tipo_negocio']
    list_per_page = 10



admin.site.register(tipo_negocio)
admin.site.register(negocio, negociosAdmin)
