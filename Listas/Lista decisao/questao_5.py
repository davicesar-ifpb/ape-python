salarioMinimo = 1412
totalVendas = float(input("Digite o valor total das vendas: "))
comissao = totalVendas * 0.05

if comissao < salarioMinimo:
    print(f"Salário: R${salarioMinimo}")
else:
    print(f"Salário: R${comissao}")
