import pandas as pd
from sklearn.svm import LinearSVC #cerebro
from sklearn.metrics import accuracy_score #medição de precisão
from sklearn.model_selection import train_test_split #divisão das listas

######################recebendo a lista .csv######################################
uri = "https://gist.githubusercontent.com/guilhermesilveira/2d2efa37d66b6c84a722ea627a897ced/raw/10968b997d885cbded1c92938c7a9912ba41c615/tracking.csv"
dado = pd.read_csv(uri)
#print("5 primeiros clientes")
#print(dado.head())#ler os 5 primeiros
#print("5 clientes aleatorio")
#print(dado.sample(5))#ler os 5 aleatorios
#Teste pratico de um algoritmo que tenta prever se o cliente irá comprar o produto apenas observando seu comportamento no
#site. Nesse caso o x (variaveis de entrada) são os acessos a: home, how_it_works e contacts; e o y (saida) é o 
#bougth (compra)
x = dado[["home", "how_it_works", "contact"]]
y = dado[["bought"]]
#print("Variaveis de comportamento: ")
#print(x.head())#primeiros 5 itens da lista
#print("Variaveis de resposta: ")
#print(y.head())#primeiros 5 itens da lista

#################################Treinamento do algoritmo########################
modelo = LinearSVC()
treino_x, teste_x, treino_y, teste_y = train_test_split(x, y)#Quebra a lista princial em novas listas (25% para os testes). 
#Uma função que retorna 4 valores e são colocados na ordem correta da atribuição
modelo.fit(treino_x, treino_y.values.ravel()) #treina o modelo com as listas x e suas equivalentes y para criar o algoritmo de resposta
#treino_y mudei para treino_y.values.ravel() fonte: stackoverflow
previsoes = modelo.predict(teste_x)#testa o modelo (preve o y com base no x de entrada) se tiver com as mesmas variaveis usadas 
#no treino (gera uma falsa 'inteligencia') mas não é caso pois dividimos a lista
print("acerto de {:.2f}%".format(accuracy_score(teste_y, previsoes)*100))
##############Informações sobre as listas###########################
print("treino_x: {}".format(treino_x.shape))
print("treino_y: {}".format(treino_y.shape))
print("teste_x: {}".format(teste_x.shape))
print("teste_y: {}".format(teste_y.shape))