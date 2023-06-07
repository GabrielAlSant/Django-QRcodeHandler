from django.db import models


class Produto(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=50)
    preco = models.IntegerField(null=False)
    img = models.TextField(max_length=99999)

class ProdutoCarrinho(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=50)
    preco = models.IntegerField(null=False)
    img = models.TextField(max_length=99999)
