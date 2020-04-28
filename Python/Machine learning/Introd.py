#pelo longo? perna curta? faz auau? rabo enrolado?
porco1 = [0, 1, 0, 0]
porco2 = [1, 1, 0, 1]
porco3 = [0, 1, 0, 1]

cao1 = [1, 1, 1, 0]
cao2 = [0, 0, 1, 1]
cao3 = [1, 0, 0, 1]

treino_x = [porco1, porco2, porco3, cao1, cao2, cao3]
treino_y = [1, 1, 1, 0, 0, 0] #porco = 1; cao = 0

from sklearn.svm import LinearSVC #modelo de cerebro vazio
modelo = LinearSVC()
modelo.fit(treino_x, treino_y)#treina o cerebro com as informações passadas nos parametros
x = bool(input("Tem pelo longo? "))
y = bool(input("Tem perna curta? "))
z = bool(input("Ele late? "))
w = bool(input("Tem rabo enrolado? "))
animal = [x, y, z, w]
teste = modelo.predict([animal]) #recebe em lista e retorna em lista
if teste[0]== 0:
    print("É um cachorro!")
else:
    print("É um porco!")