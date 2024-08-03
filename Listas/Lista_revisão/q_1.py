VALOR_CUPOM = 30

# Entrada de dados -------------------------------

saldo = float(input())

# Calculos ---------------------------------------

quantidade_cupons = saldo // VALOR_CUPOM

# Prints -----------------------------------------

print(int(quantidade_cupons), "cupons")