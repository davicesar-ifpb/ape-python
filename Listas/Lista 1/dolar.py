import requests

requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL")
requisicao_dic = requisicao.json()
cotacao = requisicao_dic["USDBRL"]["bid"]

dolar_user = float(input("Digite quantos dolares que converter: "))
print(f"Valor em real: R${dolar_user * float(cotacao):.2f}")

