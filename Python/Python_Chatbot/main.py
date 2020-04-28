import json
from Chatbot import Chatbot

callBot = str(input("Com quem deseja falar? "))
bot = Chatbot(callBot)

while True:
    frase = bot.escuta()
    resp = bot.pensa(frase)
    print(f'{bot.nome}: {bot.fala(resp)}')
    if resp == 'tchau':
        break