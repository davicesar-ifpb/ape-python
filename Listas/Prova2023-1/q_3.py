soma_idades = 0
qtd_pesquisas = 0
qtd_pessoas_18_e_salario_1500 = 0

while True:
    idade = int(input("Digite sua idade: "))
    
    if idade == 0:
        break

    soma_idades += idade
    
    if qtd_pesquisas == 0:
        menor_salario = salario = float(input("Digite seu salário: "))
    else:
        salario = float(input("Digite seu salário: "))
    
    if salario < menor_salario:
        menor_salario = salario

    if idade == 18 and salario <= 1500:
        qtd_pessoas_18_e_salario_1500 += 1
    
    qtd_pesquisas += 1

if qtd_pesquisas == 0:
    print("Quantidade insuficiente")
else:
    print(f"Media das idades = {soma_idades/qtd_pesquisas:.2f}")
    print(f"Menor salário = {menor_salario}")
    print(f"A quantidade de pessoas com idade de 18 anos e salários até R$ 1.500,00: {qtd_pessoas_18_e_salario_1500}")
