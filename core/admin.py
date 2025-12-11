from django.contrib import admin
from .models import Unidade, Sala, Status,  Bem, Categoria
@admin.register(Unidade)
class UnidadeAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'endereco')
    search_fields = ('nome',)

@admin.register(Sala)
class SalaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'unidade')
    list_filter = ('unidade',)
  

@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ("id", "nome")

@admin.register(Bem)
class BemAdmin(admin.ModelAdmin):    
    list_display = ('id', 'nome',"tombo", 'sala', 'status', 'unidade')
    list_filter = ("unidade", "sala", "status")
    search_fields = ("nome", "tombo")

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'categoria')
    search_fields = ('nome',)