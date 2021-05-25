from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Produto, Cliente


class ProdutoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque')


class ClienteAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('nome','sobrenome','email')


admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Cliente, ClienteAdmin)

