from lib.interface import cabeçalho, menu, leia_int
from lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivo_existe(arq):
    criar_arquivo(arq)

cabeçalho('SISTEMA ARQUIVO 1.0')
while True:
    resp = menu(['Ver cadatros', 'Cadastrar Pessoas', 'Sair do sistema'])
    if resp == 1:
        ler_arquivo(arq)
    elif resp == 2:
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leia_int('Idade: ')
        cadastrar(arq, nome, idade)
    elif resp == 3:
        cabeçalho('Saindo do sistema... Até logo')
        break
    else:
        print('ERRO! Digite uma opção válida!')
    
    sleep(1)