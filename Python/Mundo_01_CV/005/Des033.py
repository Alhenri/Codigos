a = int(input("Digite um numero: "))
b = int(input("Digite outro numero: "))
c = int(input("Digite outro numero: "))
#verificando quem é menor
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
#verificando quem e maior
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print("Menor numero: {}".format(menor))
print("Maior numero: {}".format(maior))