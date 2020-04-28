n = int(input("Digite um numero para calcular o fatorial: "))
fator = n
while n>1:
    fator = fator*(n-1)
    n= n-1
print("O fatorial é {}".format(fator))