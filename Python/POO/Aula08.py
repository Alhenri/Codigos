#Agregação, uma classe usa outra como parte de si e precisa da outra
#Exemplo do carro e as rodas, o carro existe sem a roda mas nao funciona sem ela
class CarrinhoDeCompas: #Esse é um exemplo de agregação, a classe carrinho existe, porem ela precisa de produto
    def __init__(self): #para fazer as operações existentes
        self.produtos = list()

    def inserir_produto(self, produto): #metodo que irá receber um objeto inteiro
        self.produtos.append(produto) #adiciona o objeto na lista
    
    def lista_produto(self): #metodo que mostra a lista de produtos
        for produto in self.produtos: #para cada objeto na lista de objetos
            print(produto.nome, produto.valor) #mostre suas propriedades
    
    def soma_total(self):
        total = 0
        for produto in self.produtos:
            total += produto.valor
        return total

class Produto: #classe independente que cria os produtos
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor