from django.contrib import admin
from .models import Empresa, Beacon, Promocion

class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('descripcion',)

admin.site.register(Empresa, EmpresaAdmin)


class PromocionAdmin(admin.ModelAdmin):
    list_display = ('empresa','descripcion','imagen','beacon')

admin.site.register(Promocion, PromocionAdmin)


class BeaconAdmin(admin.ModelAdmin):
    list_display = ('descripcion',)

admin.site.register(Beacon, BeaconAdmin)