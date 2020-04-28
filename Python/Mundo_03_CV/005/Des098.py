from time import sleep
def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    if inicio <= fim:
        if passo > 0:
            while inicio <= fim:
                print(f'{inicio}... ', end='', flush=True)#para nao criar um buf de tela
                inicio += passo
                sleep(0.5)
            print('FIM!')
        elif passo < 0:
            while inicio <= fim:
                print(f'{fim}... ', end='', flush=True)
                fim += passo
                sleep(0.5)
            print('FIM!')
    elif inicio >= fim:
        if passo > 0:
            while inicio >= fim:
                print(f'{inicio}... ', end='', flush=True)
                inicio -= passo
                sleep(0.5)
            print('FIM!')
        if passo < 0:
            while inicio >= fim:
                print(f'{inicio}... ', end='', flush=True)
                inicio -= passo
                sleep(0.5)
#contador(0, 10, 1)
#contador(10, 0, 2)
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)