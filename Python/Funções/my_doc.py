def ler_txt(arq, lista=list()):
    """
    =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    -->> Metodo que ler todo um arquivo txt e retorna uma lista com cada linha em um dicionário
    >: arq: nome do arquivo txt
    >: lista: lista que receberá em ordem as keys do dicionario
    =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
                                Created by Alexandre H. S. S. FH.
    =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-="""
    elementos = list()
    try:
        a = open(arq, 'rt')
    except:
        print('-='*30)
        print('ERRO AO LER O ARQUIVO!!!'.center(60))
        print('Talvez o arquivo não exista ou está no diretório errado'.center(60))
        print('-='*30)
    else:
        for linha in a:
            dicio = dict()
            dado = linha.split(';')
            for p, c in enumerate(dado):
                if p == (len(dado)-1):
                    c = c.replace('\n', '')
                if c.isnumeric():
                    c = float(c)
                dicio[lista[p]] = c
            elementos.append(dicio.copy())
        a.close()
    finally:
        return elementos
def escreve_txt(arq, lista=list()):
    """
    =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    -->> Metodo que adiciona elementos ao arquivo txt
    >: arq: nome do arquivo txt
    >: lista: lista que recebera os elementos de uma mesma linha (deve acompanhar a ordem
       que foi iniciada.)
    EX: (arq = 'documento.txt, ['Geraldo', '38', 'Masculino'])
    =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
                                Created by Alexandre H. S. S. FH.
    =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-="""
    try:
        a = open(arq, 'at')
    except:
        print('-='*30)
        print('ERRO AO ABRIR O ARQUIVO!!!'.center(60))
        print('Talvez o arquivo não exista ou está no diretório errado'.center(60))
        print('-='*30)
    else:
        for p, c in enumerate(lista):#cada elemento da lista contem um dado que será posto na linha
            if p == len(lista)-1:#na ultima informação será adicionado o pula-linha
                a.write(f'{c}\n')
            else:#enquanto não chega na ultima eu coloco ';'
                try: #tento adicionar elemento ao documento
                    a.write(f'{c};')
                except:
                    print('-='*30)
                    print('ERRO AO ADICIONAR ELEMENTO NO ARQUIVO!!!'.center(60))
                    print('Talvez o arquivo não exista ou está no diretório errado'.center(60))
                    print('-='*30)
        a.close()

def criar_txt(arq):
    try:
        open(arq+'.txt', 'wt+')
    except:
        print('-='*30)
        print('ERRO AO CRIAR ARQUIVO'.center(60))
        print('Talvez o arquivo já exista'.center(60))
        print('-='*30)