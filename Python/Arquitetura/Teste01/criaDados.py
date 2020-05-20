class Pessoa:
    def __init__(self, nome, sobrenome, idade,):
        self.nome = nome
        self.idade = idade
        self.sobrenome = sobrenome
    def nomeCompleto(self):
        return self.nome + self.sobrenome
    def anoNascimento(self):
        return 2020 - int(self.idade)