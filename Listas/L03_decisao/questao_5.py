""" A empresa Vende Tudo Ltda paga o salário de cada vendedor com uma comissão de 5% sobre o
total de vendas daquele vendedor, mas essa comissão nunca deve ser inferior ao salário-
mínimo. Escreva um programa que leia o valor total das vendas de um vendedor e escreva seu
salário. """


salarioMinimo = 1412
totalVendas = float(input("Digite o valor total das vendas: "))
comissao = totalVendas * 0.05

if comissao < salarioMinimo:
    print(f"Salário: R${salarioMinimo}")
else:
    print(f"Salário: R${comissao}")
