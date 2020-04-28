"""
public: metodos e atributos que podem ser acessados dentro e fora da classe
>: A variavel é normalmente publica e por filosofia, não é privatizada
protected: metodos e atributos que so podem ser usados dentro da classe ou de suas filhas
>: por convenção, se utiliza o '_' na frente da variavel, ainda poderá ser acessada, mas o editor nao recomenda
private: metodos e atributos que so estão disponiveis dentro da classe
>: por convenção, se utiliza '__' não da pra ser acessada normalmente, deverá ser acessada, por exemplo a variavel
>: self.__dados -->  self._NomeDaClasse__dados, caso tente acessar da maneira tradicional, o interpretador criará outra variavel
"""

class Base_dados:
    def __init__(self):
        self.__dados = dict()

    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})

    def lista_clientes(self):
        for id, nome in self.__dados['clientes']. items():
            print(id, nome)

    def apaga_cliente(self, id):
        del self.__dados['clientes'][id]


bd = Base_dados()

bd.inserir_cliente(1, 'Otávio')
bd.inserir_cliente(2, 'Miranda')
bd.inserir_cliente(3, 'Alexandre')
bd.apaga_cliente(2)
# Exemplo
bd._Base_dados__dados = 'Outra coisa'
#bd.lista_clientes()
print(bd._Base_dados__dados)