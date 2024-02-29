from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math


chrome_options = Options()
chrome_options.add_argument("--headless")
service = Service(r'C:\Users\Luann\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe')
driver = webdriver.Chrome(service=service, options=chrome_options)

url = 'https://apprendafixa.com.br/app/investimentos/rendafixa'

# Carregar a página
driver.get(url)

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.CLASS_NAME, 'mat-paginator-range-label'))
    )

    range_label_text = element.text.strip()
    index = range_label_text.find('de ')
    qtd_itens = range_label_text[index + 3 :]
    ultima_pagina = math.ceil(int(qtd_itens)/ 80)


except Exception as e:
    print("Erro:", e)

finally:
    driver.quit()
