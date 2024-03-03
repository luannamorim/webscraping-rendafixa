# Web Scraping Produtos Renda Fixa

Este é um projeto de web scraping para extrair informações de produtos de renda fixa do site App Renda Fixa.

## Descrição

O objetivo deste projeto é extrair informações como nome do produto, rendimento, prazo, etc., dos produtos de renda fixa listados no site App Renda Fixa. Isso pode ser útil para análise de investimentos ou qualquer outra finalidade que exija acesso a esses dados.

## Requisitos

- Python 3.x
- Chromedriver
- Bibliotecas Python: Selenium, Pandas

## Instalação

1. Certifique-se de ter o Python 3.x instalado. Você pode baixá-lo em [python.org](https://www.python.org/downloads/).

2. Baixe a versão compatível do Chromedriver no [site oficial do Chrome for Testing](https://googlechromelabs.github.io/chrome-for-testing/#stable).

3. Clone este repositório:

    ```
    git clone https://github.com/seu-usuario/RendaFixa-Scraper.git
    ```

4. Instale as bibliotecas Python necessárias:

    ```
    pip install -r requirements.txt
    ```

## Uso

1. Certifique-se de ter o Chromedriver no diretório correto ou adicione-o ao PATH do sistema.

2. Execute o script `extract_info.py` para iniciar a extração de informações dos produtos de renda fixa do site.

    ```
    python extract_info.py
    ```

3. Os dados extraídos serão salvos em um arquivo CSV chamado `dados_extraidos.csv`.

## Contribuição

Contribuições são bem-vindas! Se você encontrar bugs ou tiver sugestões de melhorias, sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Aviso Legal

Este projeto é apenas para fins educacionais e de aprendizado. Respeite os termos de serviço do site que você está acessando.
