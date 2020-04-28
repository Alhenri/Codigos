extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez')
while True:
    while True:
        n = int(input("Digite um numero de 0 a 10: "))
        if 0 <= n <= 10: # equivalente: n <= 10 and n >= 0:
            break
        print("Numero inválido")
    print(f'O numero {n} por extenso é {extenso[n]}')
    resp = str(input("Deseja continuar? [s/n]: ")).lower()
    if resp == 'n':
        break