from django.db import models


class Produto (models.Model):
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('Preco', decimal_places=2, max_digits=8)
    estoque = models.DecimalField('Quantidade em estoque', decimal_places=2, max_digits=8)

    def __str__(self):
        return f' {self.nome}, {self.estoque}'


class Cliente (models.Model):
    nome = models.CharField('Nome', max_length=100)
    sobrenome = models.CharField('Sobrenome', max_length=100)
    email = models.EmailField('E-mail', max_length=100)

    def __str__(self):
        return f'{self.nome},{self.sobrenome}'


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField('Book name', max_length=100)
    author = models.ForeignKey(Author, blank=True, null=True)
    author_email = models.EmailField('Author email', max_length=75, blank=True)
    imported = models.BooleanField(default=False)
    published = models.DateField('Published', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    categories = models.ManyToManyField(Category, blank=True)

    def __str__(self):
        return self.name



