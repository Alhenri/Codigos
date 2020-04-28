class Pessoa: #sempre que instaciar a classe, o metodo init é chamado
    ano_atual = 2020 #é uma variavel idependente do instanciamento mas deve ser chamando como self

    def __init__(self, nome, idade, comendo=False, falando=False):#self recebe o instaciamento
        self.nome = nome #para declarações de variaveis que podem ser externas é necessario
        self.idade = idade #utilizar o self, caso o contrario, ela somente sera valida dentro 
        self.comendo = comendo #do metodo. alem disso, as variaveis self podem ser acessadas de
        self.falando = falando #outros escopos

    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} já está comendo.')
            return #so assim ele para de executar o método
        print(f'{self.nome} está comendo {alimento}')
        self.comendo = True
    
    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo.')
            return
        
        print(f'{self.nome} parou de comer.')
        self.comendo = False
    
    def get_ano_nascimento(self):
        return self.ano_atual - self.idade

    @classmethod #decorador usado geralmente como construtor alternativo
    #ele é um metodo que recebe como parametro a propria classe inves de uma instancia
    def por_ano_de_nasc(cls, nome, ano_nascimento):#cls será enviada quando for chamada o nome da classe
        idade = cls.ano_atual - ano_nascimento #calcula a idade
        return cls(nome, idade)#retorna o objeto adaptado ao init
        #exemplo de construção Pessoa.por_ano_de_ nasc('Nome', idade)

    @staticmethod #é um metodo que é simplismente uma função
    def gera_id():#pode ser utilizada dentro(sem referencia ao objeto) e fora da classe(com referencia ao objeto ou a classe)
        from random import randint
        id = randint(100, 999)
        return id #essa função pode receber parametros, mas não poderá ser usado referencias de objetos dentro

ex1 = Pessoa('\nAlexandre', 19)#pessoa criada pelo metodo __init__
ex1.comer('Laranja')

print()

ex2 = Pessoa.por_ano_de_nasc('Henrique', 2001)#pessoa criada por um classmethod
ex2.comer('Uva')

print(Pessoa.gera_id())#utiliza um staticmethod da classe