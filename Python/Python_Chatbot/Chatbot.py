import json
import sys
class Chatbot(): #cria uma clase

    def __init__(self, nome):
        try:
            memoria = open(nome+'.json', 'r')#abre para ler oque tem na memoria do bot
        except FileNotFoundError:
            memoria = open(nome+'.json', 'w')
            lista = []
            json.dump(lista, memoria)
            memoria.close()
            print('>: Bot criado com sucesso')
            memoria = open(nome+'.json', 'r')#abre para ler oque tem na memoria do bot

        self.nome = nome #self é uma refencia a si mesmo como classe (fora do programa se atibuem
        #variaveis que serão passadas como self ex: b.nome = self.nome)
        self.conhecidos = json.load(memoria) #lista de pessoas conhecidas pelo bot
        memoria.close()
        self.historico = [] #declarei uma lista
        self.frases = { 'oi': 'Olá, qual seu nome?','tchau': 'tchau'}

    def escuta(self):
        #pass #utilizado para nao da erro de identação em codigo vazio
        frase = str(input(">: "))
        frase = frase.lower()
        frase = frase.replace('é', 'eh')
        return frase

    def pensa(self, frase):
        
        if frase in self.frases:
            return self.frases[frase]
        if self.historico[-1] == 'Olá, qual seu nome?':
            nome = self.pegaNome(frase)
            resp = self.respondeNome(nome)
            return resp
        else:
            try:
                resp = str(eval(frase))#interpreta um codigo python
                return resp
            except:
                print(self.nome+': Não sei como responder, pode me dizer oque? ')
                resp = input(">: ")
                self.frases[frase] = resp
                return 'Acho que aprendi :)'

    def pegaNome(self, nome):
        if 'o meu nome eh' in nome:
            nome = nome[14:]
        nome = nome.title()
        return nome

    def respondeNome(self, nome):
        if nome in self.conhecidos:
            frase = 'Eaew '
            frase2 = ', bom te ver denovo!'
        else:
            frase = 'Muito prazer '
            self.conhecidos.append(nome)
            memoria = open(self.nome+'.json', 'w')#abre para escrever
            json.dump(self.conhecidos, memoria)
            memoria.close()
            frase2 = ', seja bem vindo!'
        return frase + nome + frase2

    def fala(self, frase): #define um função da classe
        import os
        if 'executa ' in frase:
            plataforma = sys.platform
            comando = frase.replace('executa ', '')
            if 'win' in plataforma:
                os.startfile(comando)
            elif 'linux' in plataforma:
                import subprocess as se
                try:
                    se.Popen(comando)
                except FileNotFoundError:
                    se.Popen(['xdg-open', comando])
        else:
            print(frase)
        self.historico.append(frase)#inclui elementos na lista historico
        return frase
