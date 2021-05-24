from django.contrib import admin
from core.models import Book

from .models import Produto, Cliente


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque')


class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome','sobrenome','email')


class BookResource(admin.ModelResource):

    class Meta:
        model = Book


admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Cliente, ClienteAdmin)

