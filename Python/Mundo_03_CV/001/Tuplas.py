#As tuplas são imutaveis
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata')
############## Uso do for #####################
print("~"*60)
for pos, comid in enumerate(lanche):
    print(f'Eu vou comer {comid} na posição {pos}')
print("~"*60)
print("=-"*30)
for comida in lanche:
    print(f"Eu vou comer {comida}")
print("=-"*30)
print(".."*30)
for cont in range(0, len(lanche)):
    print(f"Eu vou comer {lanche[cont]} na posição {cont}")
print(".."*30)
############## Métodos ##############
print("><"*30)
print(f"Em ordem {sorted(lanche)}")
print("><"*30)
############## Operações #############
a = (1, 2, 3, 4)
b = (2, 5, 6, 9)
c = a + b
print(">>"*30)
print(f"{a} + {b} = {c}")
print(f"Quatidade de 2 em {c} = {c.count(2)}")
print(f"Posição do 2 = {c.index(2)}")
print(">>"*30)