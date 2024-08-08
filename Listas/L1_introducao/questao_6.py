""" Faça um programa que efetue a apresentação do valor da conversão em real (R$)
de um valor lido em dólar (US$). O algoritmo deverá solicitar o valor da cotação do
dólar e também a quantidade de dólares disponíveis com o usuário. """


cotacao = float(input("Digite a votação do dolar: "))
dolar_user = float(input("Digite quantos dolares quer converter: "))
print(f"Valor em real: R${cotacao * dolar_user}")
