def fatorial(num, show=False):
    """
    By AHSSF
    num = recebe um inteiro (obrigatorio)
    show = mostra o processo da multiplicação (opcional)
    """
    fator = 1
    texto = f''
    if show == False:
        for c in range(num, 0, -1):
            fator *= c
        return fator
    else:
        for c in range(1, num):
            fator *= c
            texto += f'{c} x '
        fator *= num
        texto += f'{num} '
        texto += f'= {fator}'
        return texto
print(fatorial(int(input('Numero: '))))
help(fatorial)