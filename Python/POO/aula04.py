
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    
    def desc(self, percent):
        self.preco = self.preco - (self.preco*(percent/100))

    #Getter
    @property
    def preco(self):#se chama com o mesmo nome da variavel e é executada depois do setter
        return self._preco #retorna o valor pra variavel
    
    #Setter
    @preco.setter
    def preco(self, valor): 
    #mesmo nome que a variavel e é executado toda vez que a variavel é chamada para atribuição
        if isinstance(valor, str):
            valor = float(valor.replace('R$', ''))
        self._preco = valor


p1 = Produto('Bermuda', 'R$60')
print(p1.preco)
p1.desc(10)
print(p1.preco)