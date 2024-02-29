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

next_page_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, "/html/body/app-root/app-main-page/mat-sidenav-container/mat-sidenav-content/div/app-rendafixa-page/div[2]/mat-paginator/div/div/div[2]/button[2]"))
)

driver.execute_script("arguments[0].click();", next_page_button)

elements = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located(
        (By.CLASS_NAME, 'mat-card-title')
    )
)

for element in elements:
    conteudo_elemento = element.text.strip()
    print(conteudo_elemento)


numero_paginas = WebDriverWait(driver, 3600).until(
    EC.presence_of_element_located(
        (By.CLASS_NAME, 'mat-paginator-range-label'))
)

range_label_text = numero_paginas.text.strip()
index = range_label_text.find('de ')
qtd_itens = range_label_text[index + 3:]
ultima_pagina = math.ceil(int(qtd_itens) / 60)

driver.quit()
