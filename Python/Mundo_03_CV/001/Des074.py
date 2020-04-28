from random import randint
numeros = (randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))
n_antMaior = 0
print(numeros)
for n in numeros:
    if n > n_antMaior:
        n_antMaior = n
print(f"Maior numero: {n_antMaior}")
n_antMenor = n_antMaior
for n in numeros:
    if n < n_antMenor:
        n_antMenor = n
print(f"Menor numero: {n_antMenor}")
############Resolução guanabara###############
#   max(numeros), min(numeros) retorna o maior e o menor numero da tupla