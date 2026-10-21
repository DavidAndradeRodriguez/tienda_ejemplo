from django.contrib import admin
from shop.models import producto, categoria
# Register your models here.

admin.site.register(producto)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'producto')
    search_fields = ('nombre', 'descripcion', 'producto__nombre')
    list_filter = ('producto',)
    ordering = ('nombre',)

admin.site.register(categoria, CategoriaAdmin)
class categoriaInline(admin.TabularInline):
    model = categoria
    extra = 1