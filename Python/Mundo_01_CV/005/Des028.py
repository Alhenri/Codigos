import random
n1 = random.randint(0,5)
n2 = int(input("Digite um numero de 0 a 5: "))
if n1 == n2:
    print("Você ganhou!")
else:
    print("Você perdeu!")
print("Numero sorteado {}".format(n1))