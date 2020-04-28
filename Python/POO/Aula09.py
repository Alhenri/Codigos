#Numa composição, uma classe pertence a outra, quando uma morrer, a outra morre
class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.enderecos = list()

    def isere_enderec(self, cidade, estado):
        self.enderecos.append(Endereco(cidade, estado))#instancia da classe endereço que pertence a classe Cliente

    def lista_enderecos(self):
        for ende in self.enderecos:
            print(ende.cidade, ende.estado)

    def __del__(self):
        print(f'{self.nome} foi apagado')

class Endereco:
    def __init__(self, cidade, estado):
        self.cidade = cidade
        self.estado = estado
    
    def __del__(self): #executa quando o programa apaga a classe(geralmente no fim do programa)
        print(f'{self.cidade} foi apagado')

c1 = Cliente('Alexandre', 19)
c1.isere_enderec('Abreu e Lima', 'PE')
print(c1.nome)
c1.lista_enderecos()
del c1 #veja que alem do objeto c1, o objeto endereço tambem é apagado
print()

c2 = Cliente('João', 22)
c2.isere_enderec('São Paulo', 'SP')
print(c2.nome)
c2.lista_enderecos()

print('=-'*30)