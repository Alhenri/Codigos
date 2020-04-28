import random as r
print("##### Bem-vindo ao Jokenpô #####")
print("1- Pedra")
print("2- Papel")
print("3- Tesoura")
op = int(input("Faça sua escolha: "))
pc = r.randint(1,3)
nome = ['Pedra', 'Papel', 'Tesoura']
if op == pc:
    print("Computador: {}".format(nome[pc-1]))
    print("Humano: {}".format(nome[op-1]))
    print("Resultado: Empate!!")
elif (op == 1 and pc==3) or (op == 2 and pc == 1) or (op == 3 and pc == 2):
    print("Computador: {}".format(nome[pc-1]))
    print("Humano: {}".format(nome[op-1]))
    print("Humano venceu!!")
else:
    print("Computador: {}".format(nome[pc-1]))
    print("Humano: {}".format(nome[op-1]))
    print("Computador venceu!!")