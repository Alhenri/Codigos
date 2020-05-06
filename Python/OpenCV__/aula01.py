from cv2 import cv2
import numpy as np  # biblioteca responsavel por trabalhar com matrizes e arrays multidimensionais
from matplotlib import pyplot as plt  # Vamos usar pra plotar as imagens em formato de matriz do numpy


def showImage(img):
    #o opencv guarda os valores de RGB numa ordem diferente da matplotlib
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #troca a ordem de brg para rgb
    plt.imshow(img)#constroi a janela gráfica com a matriz
    plt.show()

def getColor(img, y, x):
    return img.item(y, x, 0), img.item(y, x, 1), img.item(y, x, 2)

def setColor(img, y, x, b, g, r):
    img.itemset((y, x, 0), b)
    img.itemset((y, x, 1), g)
    img.itemset((y, x, 2), r)

    return img

def main():
    obj_img = cv2.imread("Desert.jpg")#o segundo parametro (0) passa a imagem com tons de cinza então o shape
    # so passará parametros
    altura, largura, canais_de_cor = obj_img.shape #é um vetor 3d que mostra a largura da imagem, altura e quantos canais de cores tem
    #print(f'Dimensões: {str(largura)}x{str(altura)}')
    #print(f'Canais de cor: {str(canais_de_cor)}')

    for y in range(0, altura): #percorrer as linhas da imagem
        for x in range(0, largura): #percorrer as colunas da imagem
            #Agora tenho acesso aos pixels da imagem por meio da img[y][x] que retorna uma tupla com os 3 valores de BGR
            # azul = img.item(y, x, 0)#passa as cordenadas do pixel e o canal de cor irá retornar o intensidade da cor
            # verde = img.item(y, x, 1)
            # vermelho = img.item(y, x, 2)
            #obj_img.itemset((y, x, 0), 0)#primeiro parametro é a cor de determinado pixel, e a segunda é o novo valor dele
            azul, verde, vermelho = getColor(obj_img, y, x)
            #obj_img = setColor(obj_img, y, x, 0, verde, vermelho)
    
    obj_mont = obj_img[300 : 350, 170 : 220]# Pegando um trecho da imagem original
    obj_img[50 : 50 + obj_mont.shape[0], 70 : 70 + obj_mont.shape[1]] = obj_mont

    showImage(obj_img)
    #cv2.imwrite("Modificado.jpg", obj_img)

main()