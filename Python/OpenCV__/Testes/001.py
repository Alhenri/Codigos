import cv2
from matplotlib import pyplot as plt

obj_img = cv2.imread("Desert.jpg")
obj_img = cv2.cvtColor(obj_img, cv2.COLOR_BGR2RGB)
altura, largura, canais = obj_img.shape
obj_gmi_largura = list()
obj_gmi = list()
for y in range(altura-1, 1, -1):
    for x in range(largura-1, 1, -1):
        obj_gmi_largura.append(obj_img[y][x])
    obj_gmi.append(obj_gmi_largura)
    obj_gmi_largura.clear()
