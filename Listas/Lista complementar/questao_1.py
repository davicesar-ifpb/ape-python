""" A Companhia de Carros Usados João Honesto paga seus empregados um salário de R$
1.000,00 por mês mais uma comissão de R$ 200,00 por cada carro vendido mais 5% do
valor da venda.
Escreva um programa que leia o nome, o número de carros vendidos e o valor total das
vendas de um vendedor, e calcule e exiba o seu salário. """


salario = 1_000
comissao = 200

nome = input("Digite seu nome: ")
quantidade_carros = int(input("Digite a quantidade de carros vendidos: "))
total_vendas = float(input("Digite o valor total das vendas: "))
salario_final = salario + (comissao * quantidade_carros) + (total_vendas * 0.05)

print(f"{nome}, o seu salário é: R${salario_final}")