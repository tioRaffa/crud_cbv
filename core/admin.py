from django.contrib import admin
from .models import ProdutoModel
# Register your models here.

@admin.register(ProdutoModel)
class ProdutoModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price']