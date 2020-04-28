#help()#metodo que retorna informações de funções jogadas no seu argumento (docstring)
#print(input.__doc__)#__doc__ retorna informações sobre a função que o chama

##Criando uma docstring##
def escreva(a):
    """
    Essa eh a docstring
    """
    print('-'*10)
    print(a)
help(escreva)

##Parametro opcional##
# Se usa para definir parametros padrão a determinados metodos e evitar erros por falta deles
def somar(a=0, b=0, c=0):
    s = a+b+c
    print(f'A soma vale {s}')
somar(2,4)#mesmo passando apenas 2 parametros, a função está correta
somar(a=8, c=1)#passar os parametros fora de ordem

##Escopo de variaveis
#As variaveis existem em ordem de identação
def teste(b):
    global z #fala pra o interpretador nao criar um nova variavel e sim pegar a global já existente
    z = 8
    b += 4
    c = 2
    print(f'z dentro vale {z}')
    print(f'b dentro vale {b}')
    print(f'c dentro vale {c}')
z = 5
teste(z)
print(f'z fora vale {z}')