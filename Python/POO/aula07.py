#Faremos uma classe conversar com outra classe, elas estarão associadas
class Escritor:
    def __init__(self, nome):
        self.__nome = nome
        self.__ferramenta = None

    @property
    def nome(self):#usado para poder ver o que ta escrito na variavel privada
        return self.__nome

    @property
    def ferramenta(self): #metodo usado para ler oq está dentro da variavel privada
        return self.__ferramenta

    @ferramenta.setter #metodo usado para modificar oq está na variavel privada
    def ferramenta(self, ferramenta):
        self.__ferramenta = ferramenta

class Caneta:
    def __init__(self, marca):
        self.__marca = marca

    @property
    def marca(self):
        return self.__marca

    def escrever(self):
        print('Caneta está escrevendo...')

class Maquina:
    def escrever(self):
        print('Maquina está escrevendo...')


escritor = Escritor('Alexandre') #cria o objeto escritor
caneta = Caneta('Bic') #cria o objeto caneta

escritor.ferramenta = caneta #pega TODO o objeto da caneta e joga numa variavel
escritor.ferramenta.escrever() #apartir dai, pode-se usar os métodos do objeto jogado dentro da variavel
print(escritor.ferramenta.marca)