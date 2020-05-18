from selenium.webdriver.opera.options import Options
import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
import json

#1. Pegar conteudo HTML a partir da URL
url = "https://stats.nba.com/players/traditional/?PerMode=Totals&Season=2019-20&SeasonType=Regular%20Season&sort=PLAYER_NAME&dir=-1"
local = r"C:\Users\Usuario\Documents\operadriver.exe" #precisa do 'r' pra indicar o caminho
option = Options() #instaciando a classe Option
option.headless = False #headless é pra nao mostra o programa aberto
driver = webdriver.Opera(executable_path=local, options=option)
driver.get(url)

time.sleep(10)

driver.find_element_by_xpath(
        "//div[@class='nba-stat-table']//table//thead//tr//th[@data-field='PTS']").click()#Procura o caminho do elemento e clica nele

element = driver.find_element_by_xpath("//div[@class='nba-stat-table']//table")
html_content = element.get_attribute('outerHTML')

# 2. Parsear o conteúdo HTML - BeatifulSoup
#Faz anpalise do html e tranforma num dado estruturado
soup = BeautifulSoup(html_content, 'html.parser')
table = soup.find(name='table')

# 3. Estruturar conteudo em um Data Frame - Pandas
df_full = pd.read_html(str(table))[0].head(10)

df = df_full[['Unnamed: 0', 'PLAYER', 'TEAM', 'PTS']]
df.columns = ['pos', 'player', 'team', 'total']

# 4. Transformar os dado num dicionario
top10ranking = dict()
top10ranking['points'] = df.to_dict('records')
driver.quit()

# 5. Salvar tudo num arquivo JSON
js = json.dumps(top10ranking)
fp = open('ranking.json', 'w')
fp.write(js)
fp.close()