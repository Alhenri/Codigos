import requests
import json

r = requests.get('https://reactflix-ahssf.herokuapp.com/categorias').text
r = json.loads(r)

for c in r:
    print(c["nome"])