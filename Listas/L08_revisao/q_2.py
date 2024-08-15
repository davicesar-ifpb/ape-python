VALOR_CUPOM = 30

# Entrada de dados -------------------------------

saldo = float(input())

# Calculos ---------------------------------------

quantidade_cupons = saldo // VALOR_CUPOM
saldo_restante = saldo % VALOR_CUPOM
falta_para_cupom = VALOR_CUPOM - (saldo % VALOR_CUPOM)

# Prints -----------------------------------------

if quantidade_cupons == 0:
    quantidade_cupons = "Sem cupons"
else:
    print(int(quantidade_cupons), "cupons")

print(f"restante: R${saldo_restante:.2f}")
print(f"falta para o cupom: R${falta_para_cupom:.2f}")