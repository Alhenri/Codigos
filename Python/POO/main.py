from aula07 import Escritor
from aula07 import Caneta

escritor = Escritor('Alexandre')
caneta = Caneta('Bic')
print(escritor.nome)#como so recebe o parametro self, não precisa de ()
print(caneta.marca)