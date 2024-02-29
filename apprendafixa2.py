from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

chrome_options = Options()
chrome_options.add_argument("--headless")
service = Service(
    r'C:\Users\Luann\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe')
driver = webdriver.Chrome(service=service, options=chrome_options)

url = 'https://apprendafixa.com.br/app/investimentos/rendafixa'

driver.get(url)

numero_paginas = WebDriverWait(driver, 3600).until(
    EC.presence_of_element_located(
        (By.CLASS_NAME, 'mat-paginator-range-label'))
)

range_label_text = numero_paginas.text.strip()
index = range_label_text.find('de ')
qtd_itens = range_label_text[index + 3:]
ultima_pagina = math.ceil(int(qtd_itens) / 60)

elements = WebDriverWait(driver, 60).until(
    EC.presence_of_all_elements_located(
        (By.CLASS_NAME, 'card')
    )
)

data = {}

for element in elements:
    itens = element.find_elements(By.TAG_NAME, 'div')
    categoria = itens[0].text
    dados = {}
    dados['SIMPAR'] = itens[1].text
    dados['Valor Mínimo'] = itens[2].text
    dados['Rentabilidade'] = itens[3].text
    dados['Valor Líquido'] = itens[4].text
    dados['Rating do Emissor'] = itens[5].text
    dados['Vencimento'] = itens[6].text
    dados['Liquidez'] = itens[7].text
    dados['Taxa'] = itens[8].text
    dados['LCI/LCA'] = itens[9].text
    data[categoria] = dados

print(data)


driver.quit()


# next_page_button = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable(
#         (By.XPATH, "/html/body/app-root/app-main-page/mat-sidenav-container/mat-sidenav-content/div/app-rendafixa-page/div[2]/mat-paginator/div/div/div[2]/button[2]"))
# )

# driver.execute_script("arguments[0].click();", next_page_button)
