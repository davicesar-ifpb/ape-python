salarioMinimo = 1412
totalVendas = float(input("Digite o valor total das vendas: "))
salario = totalVendas * 0.05

if salario < salarioMinimo:
    print(f"Salário: R${salarioMinimo}")
else:
    print(f"Salário: R${salario}")