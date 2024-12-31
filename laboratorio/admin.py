from django.contrib import admin
from laboratorio.models import Laboratorio, DirectorGeneral, Producto
# Register your models here.

@admin.register(Laboratorio)

class LaboratorioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre',)

@admin.register(DirectorGeneral)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'laboratorio')

@admin.register(Producto)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('nombre','laboratorio', 'f_fabricacion', 'p_costo', 'p_venta')
   
    
