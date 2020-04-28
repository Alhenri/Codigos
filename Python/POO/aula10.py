"""
Associação - Usa | Agregação - Tem | Composição - É dono | Herança - É
"""

#Herança é usada pra evitar repetição de códigos que tem trechos em comum
class Pessoa:#classe generica (Super Classe)
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.classe = self.__class__.__name__ #pega o nome da classe que a ta chamando

    def falar(self):
        print(f'{self.classe} está falando...')


class Cliente(Pessoa):#classe especifica que herdou a classe Pesso
    #Essa classe possui os mesmos metodos e atributos da classe principal
    def comprar(self):
        print(f'{self.classe} está comprando...')

class Aluno(Pessoa):
    def estudar(self):#método especifico de aluno
        print(f'{self.classe} está estudando...')
##########################
c1 = Cliente('Alexandre', 19)
print(c1.nome)
print(c1.idade)
c1.falar()
c1.comprar()

a1 = Aluno('José', 22)
print(a1.nome)
print(a1.idade)
a1.falar()
a1.estudar()