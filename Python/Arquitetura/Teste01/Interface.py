import Dados
class classeInterface:
    def __init__(self):
        self.stat = False
        print('  Criando interface...')
    def openInterface(self):
        self.stat = True
        dado = Dados.retornaDados()
        print('  Jogando dados na interface...')
        print('  Abrindo interface...\n')
        print('=-=-Interface=-=-=-')
        print(f'idade: {dado.idade}')
        print(f'nome: {dado.nome}')
        print(f'nome completo: {dado.nomeCompleto()}')
        print(f'ano de nasmiento: {dado.anoNascimento()}')
        print('=-=-=-=-=-=-=-=-=-=\n')
    def fechaInterface(self):
        self.stat = False
        Dados.salvaDados()
        print('  Fechando interface...')
