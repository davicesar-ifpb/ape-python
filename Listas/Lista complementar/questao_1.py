salario = 1_000
comissao = 200

nome = input("Digite seu nome: ")
quantidade_carros = int(input("Digite a quantidade de carros vendidos: "))
total_vendas = float(input("Digite o valor total das vendas: "))
salario_final = salario + (comissao * quantidade_carros) + (total_vendas * 0.05)

print(f"{nome}, o seu salário é: R${salario_final}")