from pygame import mixer
from time import sleep
import os
mixer.init()
mixer.music.load(os.path.join(os.path.dirname(__file__), 'musica.mp3'))#passa o endereço da mesma pasta do arquivo
while True:
    mixer.music.play()
    #sleep(10) #precisa disso para continuar tocando
    if input(">: "):
        break
