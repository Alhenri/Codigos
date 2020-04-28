def leia_int(perg):
    while True:
        try:
            n = int(input(perg))
        except (ValueError, TypeError):
            print('ERRO!! Valor digitado inválido!')
        except KeyboardInterrupt:
            n = 0
            break
        else:
            break
    return n

def linha(tamanho = 42):
    return '-'*42

def cabeçalho(txt):
    print(linha())
    print(txt.center(42))#deixa o texto no centro de 42 caracteres
    print(linha())

def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    for p, c in enumerate(lista):
        print(f'{p+1} - {c}')
    print(linha())
    opc = leia_int('Sua Opção: ')
    return opc