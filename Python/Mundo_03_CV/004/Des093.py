jogador = dict()
gols = list()
total = 0
jogador['Nome'] = str(input('Nome do jogador: '))
jogador['Partidas'] = int(input('Numero de partidas jogas: '))
for c in range(1, jogador['Partidas']+1):
    n = int(input(f'Gols na partida {c}: '))
    gols.append(n)
    total += n #########Substituido pela função sum(jogador['Gols'])
jogador['Gols'] = gols
jogador['Total'] = total
print(jogador)
for c, p in enumerate(jogador['Gols']):
    print(f'Na {c+1}º partida ele fez {p} gols.')
print(f'Foram {jogador["Total"]} gols no total')