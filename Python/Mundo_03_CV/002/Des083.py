exp = str(input('Digite a expressão matematica: '))#Toda string é uma lista
a = exp.count('(')
b = exp.count(')')
if a == b:
    print('Expressão válida!')
else:
    print('Expressão inválida')