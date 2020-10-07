import json
import requests


def ler_json(arq_json):
    with open(arq_json, 'r', encoding='utf8') as f:
        return json.load(f)

arq = r'.\dados.json'
dados = ler_json(arq)

for a in range(0, 50):
    # pegando o link das imagens
    url = dados['data']['user']['edge_followed_by']['edges'][a]['node']['profile_pic_url']
    r = requests.get(url)
    # baixando imagens
    with open(f'.\imagens\img{a}.jpg', 'wb') as f:
        f.write(r.content)