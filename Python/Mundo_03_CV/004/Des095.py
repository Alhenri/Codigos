time = list()
while True:
    jogador = dict()
    gols = list()
    jogador['Nome'] = str(input('Nome do jogador: '))
    jogador['Partidas'] = int(input('Numero de partidas jogas: '))
    for c in range(1, jogador['Partidas']+1):
        n = int(input(f'Gols na partida {c}: '))
        gols.append(n)
    jogador['Gols'] = gols[:]#Precisa disso pra criar uma copia de uma lista
    jogador['Total'] = sum(gols)
    while True:
        resp = str(input('Deseja continuar? [S/N]: ')).upper()[0]
        if resp in 'SN':
            break
        print("Resposta invalida!!")
    time.append(jogador.copy())#precisa disso pra criar uma copia de uma lista
    jogador.clear()
    gols.clear()
    if resp == 'N':
        break
print('-='*30)
print('Cod   Nome            Gols                      Total')
print('-'*60)
for c, j in enumerate(time):
    print(f'{str(c):<5} {str(j["Nome"]):<15} {str(j["Gols"]):<25} {str(j["Total"]):>5}')
print('=-'*30)
while True:
    cod = int(input("Mostrar dados de qual Jogador [cod]? [999 stop]: "))
    if cod == 999:
        break
    print('-'*60)
    print(f'-- Levantamento do jogador {time[cod]["Nome"]}')
    for j, g in enumerate(time[cod]['Gols']):
        print(f'     No jogo {j+1} fez {g} gols.')
    print('=-'*30)