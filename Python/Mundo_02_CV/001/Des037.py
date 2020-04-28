numero = int(input("Digite um numero: "))
print("1- binário")
print("2- octal")
print("3- Hexa")
op = int(input("Escolha a opção que deseja converter o numero: "))
if op == 1:
    numero = bin(numero)
    print(numero)
elif op == 2:
    numero = oct(numero)
    print(numero)
elif op == 3:
    numero = hex(numero)
    print(numero)
else:
    print("Opção inexistente!")