# Projeto de Extração de Informações de Produtos de Renda Fixa do site App Renda Fixa

Este projeto tem como objetivo extrair informações de produtos de renda fixa disponíveis no site [App Renda Fixa](https://apprendafixa.com.br/app/investimentos/rendafixa) usando a biblioteca Selenium em Python.

Certifique-se de baixar a versão compatível do Chromedriver no [site oficial do Chrome for Testing](https://googlechromelabs.github.io/chrome-for-testing/#stable).

## Requisitos

- Python 3.x
- Selenium
- Chromedriver,
- Pandas

## Instalação

1. Certifique-se de ter o Python 3.x instalado. Você pode baixá-lo em [python.org](https://www.python.org/downloads/).

2. Instale a biblioteca Selenium e Pandas usando o pip:

    ```
    pip install selenium
    pip install pandas
    ```

3. Baixe a versão compatível do Chromedriver no [site oficial do Chrome for Testing](https://googlechromelabs.github.io/chrome-for-testing/#stable).

4. Certifique-se de colocar o Chromedriver no diretório correto ou adicionar o diretório do Chromedriver ao PATH do sistema.

## Uso

Execute o script `extract_info.py` para iniciar a extração de informações dos produtos de renda fixa do site.

```bash
python extract_info.py
