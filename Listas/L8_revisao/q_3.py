VALOR_CUPOM = 30
total_vendido_valor = 0
total_cupons_distribuidos = 0
maior_valor_vendido = -1
qtd_cupons_maior_valor = 0

# Entrada de dados -------------------------------
for i in range(200):
    saldo = float(input())    

# Calculos ---------------------------------------

    quantidade_cupons = saldo // VALOR_CUPOM
    saldo_restante = saldo % VALOR_CUPOM
    falta_para_cupom = VALOR_CUPOM - (saldo % VALOR_CUPOM)

    total_vendido_valor += saldo
    total_cupons_distribuidos += quantidade_cupons

    if maior_valor_vendido < saldo:
        maior_valor_vendido = saldo
        qtd_cupons_maior_valor = quantidade_cupons

# Prints -----------------------------------------

if quantidade_cupons == 0:
    quantidade_cupons = "Sem cupons"
else:
    print(int(quantidade_cupons), "cupons")

print(f"restante: R${saldo_restante:.2f}")
print(f"falta para o cupom: R${falta_para_cupom:.2f}")
print("total vendido: R$", total_vendido_valor)
print("total cupons distribuidos: ", total_cupons_distribuidos)
print("maior valor vendido: R$", maior_valor_vendido)
print("quantidade cupons maior valor: ", qtd_cupons_maior_valor)