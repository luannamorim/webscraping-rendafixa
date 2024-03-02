from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd


chrome_options = Options()
chrome_options.add_argument("--headless")

service = Service(
    r'.\chromedriver.exe')
driver = webdriver.Chrome(service=service, options=chrome_options)

url = 'https://apprendafixa.com.br/app/investimentos/rendafixa'

driver.get(url)

numero_paginas = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located(
        (By.CLASS_NAME, 'mat-paginator-range-label')))

range_label_text = numero_paginas.text.strip()
index = range_label_text.find('de ')
qtd_itens = range_label_text[index + 3:]
ultima_pagina = -(-int(qtd_itens) // 60)

print(qtd_itens, " itens disponíveis")

produtos = []

try:
    print("Extraindo informações...")
    for i in range(1, ultima_pagina+1):
        elements = WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located(
                (By.CLASS_NAME, 'card')
            )
        )

        for element in elements:
            texto = element.text.split('\n')
            produtos.append(texto)

        next_page_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, "/html/body/app-root/app-main-page/mat-sidenav-container/mat-sidenav-content/div/app-rendafixa-page/div[2]/mat-paginator/div/div/div[2]/button[2]"))
        )

        driver.execute_script("arguments[0].click();", next_page_button)

except Exception:
    pass

finally:

    driver.quit()

    for i, sublista in reversed(list(enumerate(produtos))):
        if sublista[2] != "Valor Mínimo":
            sublista.pop(0)
        elif sublista[14] != "Taxa":
            del produtos[i]

    colunas = [0, 1, 3, 5, 7, 9, 11, 13, 15, 16]
    nome_colunas = ['Produto', 'Instituição', 'Valor Mínimo', 'Rentabilidade',
                    'Valor Líquido', 'Rating do Emissor', 'Vencimento', 'Liquidez', 'Taxa', 'Detalhes']
    df = pd.DataFrame(produtos)[colunas]
    arquivo = r'.\\' + 'base_renda_fixa.csv'
    df.to_csv(arquivo, encoding='utf-8-sig', sep=';',
              index=False, header=nome_colunas)
    print("Extração finalizada!")
