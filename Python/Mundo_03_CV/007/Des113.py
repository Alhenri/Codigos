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
def leia_float(perg):
    while True:
        try:
            n = float(input(perg))
        except (ValueError, TypeError):
            print('ERRO!! Valor digitado inválido!')
        except KeyboardInterrupt:
            n = 0
            break
        else:
            break
    return n
print(leia_int('Numero inteiro: '))
print(f'{leia_float("Numero float: "):.2f}')