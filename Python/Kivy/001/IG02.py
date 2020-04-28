from kivy.app import App
from kivy.uix.button import Button #importa o botão
from kivy.uix.boxlayout import BoxLayout #Modulo responsavel pelas regras de disposição os itens na tela
from kivy.uix.label import Label
class Test(App): #classe que herda App com todas as suas funcionalidades
    def build(self): #metodo que constroi a interface
        #return Button(text='Olá Mundo') #retorna a construção do botão
        box = BoxLayout(orientation='vertical')#cria o layout vertical
        button = Button(text='Botão 1',font_size=30,on_release=self.incrementar)#cria um botão, altera o tamanho da fonte
        #e adiciona o evento de solta o botão para chamar uma função
        self.label = Label(text='1',font_size=30)
        box.add_widget(self.label)
        box.add_widget(button)#insere o botão criando no layout
        return box #retorna o layout completo

    def incrementar(self, button):#esse metodo recebe button como argumento permitindo sua modificação
        button.text = 'Soltei' #button.propriedade = novo valor
        button.font_size=200
        self.label.text = str(int(self.label.text)+1)#Intanciei o label com self. para poder ter acesso por esse metodo
        #e poder alterar suas caracteristicas, transformo para inteiro pra realizar a soma e depois pra string para
        #realizar a atribuição

Test().run()#roda a classe Test()