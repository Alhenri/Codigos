soma = 0
for c in range(0, 6):
    n = int(input("Digite um numero: "))
    if n%2 == 0:
        soma += n
print("A soma dos numeros pares é {}".format(soma))