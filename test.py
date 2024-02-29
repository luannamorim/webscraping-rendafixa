from datetime import datetime

data_atual = datetime.now()
nome_arquivo = data_atual.strftime("%Y-%m-%d") + ".csv"
caminho_arquivo = r'C:\Users\Luann\Downloads\\' + nome_arquivo

print(caminho_arquivo)
