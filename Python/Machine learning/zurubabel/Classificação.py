import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
plt.figure(figsize=(4,4))
plt.subplot(111)

#Essa função cria pontos aleatorios e as classifica de acordo como o numero de classes e o random state
#n_samples: numero de pontos
#random_state: Recebe numeros quase aleatorios, então é bom definir um valor especifico
#class_sep: mutiplicador do hipercubo que faz separar os pontos
#n_features: É mais ou menos como o numero de dimensões (Ná prática é como o numero de variaveis que faz 
# ele pertencer a determinado grupo)
X1, Y1 = make_classification(n_samples=150, n_features=2, n_redundant=0, n_informative=2,
                            n_clusters_per_class=1, random_state=3, class_sep=2, n_classes=4)


#X1[:,0] pega o primeiro elemento de cada subconjunto do array
#X1[:,1] pega o segundo elemento de cada subconjunto do array
plt.scatter(X1[:,0], X1[:,1], marker="o", c=Y1, s=25, edgecolor="k")
plt.show()

#----------------------------------------------------------------------------------------------------

from sklearn.model_selection import train_test_split #função que divide os dados de treino e teste
from sklearn.neighbors import KNeighborsClassifier #Um algoritimo de K-Nearest neighbors (KNN)
import numpy as np

knn = KNeighborsClassifier(n_neighbors = 3)#n_neighbors: quatidade de vizinho para fazer a classificação

X_train, X_test, Y_train, Y_test = train_test_split(X1, Y1, random_state=1)

knn.fit(X_train, Y_train)

print(f'Treino = {knn.score(X_train, Y_train)}')
print(f'Teste = {knn.score(X_test, Y_test)}')
#----------------------------------------------------------------------------------------------------

from matplotlib.colors import ListedColormap
x_min, x_max = X1[:,0].min() - 1, X1[:,1].max() + 1
y_min, y_max = Y1[:,0].min() - 1, Y1[:,1].max() + 1###Linha errada
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.1),
                    np.arange(y_min, y_max, 0.1))

cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF'])
cmap_bold = ListedColormap(['#FF0000', '#00FF00', '#0000FF'])

Z = knn.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
plt.figure()
plt.pcolormesh(xx, yy, Z, cmap = cmap_light)
plt.scatter(X1[:,0], X1[:,1], c=Y1, cmap = cmap_bold,
           edgecolor="k", s=20)
plt.show()