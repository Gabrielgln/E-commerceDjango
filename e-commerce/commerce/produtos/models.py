from django.db import models


# Create your models here.
class Produto(models.Model):
    description = models.CharField(max_length=50)
    value = models.IntegerField(default=0)


    def __str__(self):
        return self.description


class Carrinho:
    def __init__(self):
        self.lista = []
        self.frete = 0
        self.value = 0

    def adicionarAoCarrinho(self,produto):
        self.frete = self.frete + 10
        self.lista.append(produto)

    def removerDoCarrinho(self,produto):
        self.frete = self.frete - 10
        self.lista.remove(produto)

    def listarProdutos(self):
        for i in self.lista:
            print("{",i.description,"-",i.value,"}")

    def subTotal(self):
        for i in self.lista:
            self.value = self.value + i.value

    def valorTotalCarrinho(self):
        if self.value >= 250:
            self.frete = 0
            return self.value + self.frete
        else:
            return self.value + self.frete

    def orderByDescription(self):
        self.lista_sorted = []
        for i in self.lista:
            self.lista_sorted.append(i)
        self.lista_sorted.sort(key=lambda produto:produto.description)
        return self.lista_sorted

    def orderByValue(self):
        self.lista_sorted = []
        for i in self.lista:
            self.lista_sorted.append(i)
        self.lista_sorted.sort(key=lambda produto:produto.value)
        return self.lista_sorted

    def comprar(self):
        self.lista = []
        print("Compra realizada com sucesso!")










