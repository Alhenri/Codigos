from kivy.app import App
from kivy.uix.button import Button #importa o botão
from kivy.uix.boxlayout import BoxLayout #Modulo responsavel pelas regras de disposição os itens na tela
from kivy.uix.label import Label
class Test(App): #classe que herda App com todas as suas funcionalidades
    def build(self): #metodo que constroi a interface
        #return Button(text='Olá Mundo') #retorna a construção do botão
        box = BoxLayout(orientation='vertical')#cria o layout vertical
        button = Button(text='Botão 1')#cria um botão
        label = Label(text='Texto 1')
        box.add_widget(button)#insere o botão criando no layout
        box.add_widget(label)

        box2 = BoxLayout()#cria o layout horizontal
        button2 = Button(text='Botão 2')#cria um botão 2
        label2 = Label(text='Texto 2')
        box2.add_widget(button2)#insere o botão criando no layout2
        box2.add_widget(label2)

        box.add_widget(box2)
        return box #retorna o layout completo
Test().run()#roda a classe Test()