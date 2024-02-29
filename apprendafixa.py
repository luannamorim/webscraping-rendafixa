from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import re
import pandas as pd
from datetime import datetime

chrome_options = Options()
chrome_options.add_argument("--headless")
service = Service(
    r'C:\Users\Luann\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe')
driver = webdriver.Chrome(service=service, options=chrome_options)

url = 'https://apprendafixa.com.br/app/investimentos/rendafixa'

driver.get(url)

numero_paginas = WebDriverWait(driver, 30).until(
    EC.presence_of_element_located(
        (By.CLASS_NAME, 'mat-paginator-range-label')))

range_label_text = numero_paginas.text.strip()
index = range_label_text.find('de ')
qtd_itens = range_label_text[index + 3:]
ultima_pagina = math.ceil(int(qtd_itens) / 60)

dic_produtos = {'produto': [], 'instituição': [], 'Valor Mínimo': [], 'Rentabilidade': [], 'Valor Líquido': [],
                'Rating do Emissor': [], 'Vencimento': [], 'Liquidez': [], 'Taxa': [], 'Detalhes': []}

try:
    for i in range(1, ultima_pagina+1):
        elements = WebDriverWait(driver, 30).until(
            EC.presence_of_all_elements_located(
                (By.CLASS_NAME, 'card')
            )
        )

        print("Página " + str(i))

        for element in elements:
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

            dic_produtos['produto'].append(linhas[0])
            dic_produtos['instituição'].append(linhas[1])
            dic_produtos['Valor Mínimo'].append(linhas[3])
            dic_produtos['Rentabilidade'].append(linhas[5])
            dic_produtos['Valor Líquido'].append(linhas[7])
            dic_produtos['Rating do Emissor'].append(linhas[9])
            dic_produtos['Vencimento'].append(linhas[11])
            dic_produtos['Liquidez'].append(linhas[13])
            dic_produtos['Taxa'].append(linhas[15])
            dic_produtos['Detalhes'].append(linhas[16])

        next_page_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable(
                (By.XPATH, "/html/body/app-root/app-main-page/mat-sidenav-container/mat-sidenav-content/div/app-rendafixa-page/div[2]/mat-paginator/div/div/div[2]/button[2]"))
        )

        driver.execute_script("arguments[0].click();", next_page_button)

except Exception as e:
    print("Processo Finalizado")

finally:

    driver.quit()

    data_atual = datetime.now()
    nome_arquivo = data_atual.strftime("%Y-%m-%d") + ".csv"
    caminho_arquivo = r'C:\Users\Luann\Downloads\\' + nome_arquivo
    df = pd.DataFrame(dic_produtos)
    df.to_csv(caminho_arquivo, encoding='utf-8-sig', sep=';', index=False)
    print("Documento salvo em: " + caminho_arquivo)
