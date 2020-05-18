from selenium.webdriver.opera.options import Options
import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
import json

# 1 - Pegar o conteudo HTML
url = "https://covid.saude.gov.br"
operadrive = r"C:\Users\Usuario\Documents\operadriver.exe"
option = Options()
option.headless = True
drive = webdriver.Opera(executable_path=operadrive, options=option)
drive.get(url)#Faz o request
time.sleep(10)
element = drive.find_element_by_xpath("/html/body/app-root/ion-app/ion-router-outlet/app-home/ion-content/painel-geral-component/div/div[1]/div/div[1]")
tabelaHTML = element.get_attribute('outerHTML')

# 2 - Parsear o HTML
soup = BeautifulSoup(tabelaHTML, 'html.parser')
table = soup.find('lista-sanfona-component')

# 3 - Criar o dataframe
df_full = pd.read_html(str(table))[0].head()
print(df_full)
drive.quit()