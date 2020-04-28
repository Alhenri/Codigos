dado = list()
pessoa = list()
while True:
    print('-='*30)
    dado.append(str(input("Nome:")))
    dado.append(int(input("Peso: ")))
    print('-='*30)
    pessoa.append(dado[:])
    dado.clear()
    if input("Quer continuar? [s/n]: ").lower() == 'n':
        break

peso = list()
for p in pessoa:
    peso.append(p[1])
peso.sort()
p_pesada = list()
p_leve = list()
for p in pessoa:
    if peso[-1] == p[1]:
        p_pesada.append(p[0])
    elif peso[0] == p[1]:
        p_leve.append(p[0])
print('=-'*30)
print(f'Foram cadastradas {len(pessoa)}')
print(f'O maior peso registrado foi o de {peso[-1]} com: {p_pesada}')
print(f'O menor peso registrado foi o de {peso[0]} com: {p_leve}')
print('=-'*30)