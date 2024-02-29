from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import re

chrome_options = Options()
chrome_options.add_argument("--headless")
service = Service(
    r'C:\Users\Luann\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe')
driver = webdriver.Chrome(service=service, options=chrome_options)

url = 'https://apprendafixa.com.br/app/investimentos/rendafixa'

driver.get(url)

element = WebDriverWait(driver, 60).until(
    EC.presence_of_element_located(
        (By.CLASS_NAME, 'card')
    )
)

texto = element.text

palavras_remover = [
    "Valor Mínimo",
    "Rentabilidade",
    "Valor Líquido",
    "Rating do Emissor",
    "Vencimento",
    "Liquidez",
    "Taxa",
    "INVESTIR",
    "+ DETALHES"
]

padrao = "|".join(map(re.escape, palavras_remover))

texto_limpo = re.sub(padrao, "", texto)

linhas = texto_limpo.split('\n')
dados = [linha.strip() for linha in linhas if linha.strip()]

resultado = ', '.join(dados)

print(resultado)

driver.quit()
