def area(larg, comp):
    Area = larg*comp
    print(f'A area do terreno {larg}x{comp} é {Area}')

larg1 = int(input('Largura do terreno: '))
comp1 = int(input('Comprimento do terreno: '))
area(larg1, comp1)