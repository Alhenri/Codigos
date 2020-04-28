from lib.interface import cabeçalho

def arquivo_existe(nome):
    try:
        a = open(nome, 'rt')#read txt
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criar_arquivo(nome):
    try:
        a = open(nome, 'wt+')#leitura de arquivo txt incluindo criação
        a.close()
    except:
        print('Houve um erro ')
    else:
        print('Arquivo criado com sucesso!')

def ler_arquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('ERRO ao ler arquivo!')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        #print(a.read())#readlines: retorna uma lista com todos os elementos (cada linha) dentro do arquivo
        #read: pega todo arquivo como uma string
        for linha in a:
            dado = linha.split(';')#divide a linha em 2 onde tiver ';'
            dado[1] = dado[1].replace('\n', '')#tira o \n do final das strings
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()

def cadastrar(arq, nome='Desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um erro durante o cadastro')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro durante a inscrição')
        else:
            print(f'Novo registo de {nome} adicionado!')
        finally:
            a.close()