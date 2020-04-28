teste = list()
teste.append('Alexnadre')
teste.append(19)
galera = list()
galera.append(teste[:])
teste[0] = 'Cloe'
teste[1] = 22
galera.append(teste[:])#Lista dentro de lista
print(galera)

galera = list()
dado = list()
for c in range(0, 3):
    dado.append(str(input("Nome: ")))
    dado.append(int(input("Idade: ")))
    galera.append(dado[:])
    dado.clear()
print(galera)
for p in galera:
    print(p)