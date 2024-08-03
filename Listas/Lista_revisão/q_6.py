total_vendido_valor = 0
total_cupons_distribuidos = 0

maior_valor_vendido = -1
qtd_cupons_maior_valor = 0

receberam_todos_cupons = 0

VALOR_CUPOM = 30
estoque = 1000

# Entrada de dados -------------------------------

while estoque > 0:
    
    saldo = float(input())    

# Calculos ---------------------------------------

    quantidade_cupons = saldo // VALOR_CUPOM
    saldo_restante = saldo % VALOR_CUPOM
    falta_para_cupom = VALOR_CUPOM - (saldo % VALOR_CUPOM)

    if quantidade_cupons <= estoque:
        receberam_todos_cupons += 1
    else:
        quantidade_cupons = estoque

    if estoque > 0:
        estoque -= quantidade_cupons
    
    if maior_valor_vendido < saldo:
        maior_valor_vendido = saldo
        qtd_cupons_maior_valor = quantidade_cupons

    total_vendido_valor += saldo
    total_cupons_distribuidos += quantidade_cupons
    
# Prints -----------------------------------------

    if quantidade_cupons == 0:
        print("Sem cupons")
    else:
        print(int(quantidade_cupons), "cupons")

    print(f"saldo restante: R${saldo_restante:.2f}")
    print(f"falta para o cupom: R${falta_para_cupom:.2f}")
    
print("\ntotal vendido: R$", total_vendido_valor)
print("total cupons distribuidos:", int(total_cupons_distribuidos))
print("maior valor vendido: R$", maior_valor_vendido)
print("quantidade cupons maior valor:", int(qtd_cupons_maior_valor))
print("receberam todos os cupons:", receberam_todos_cupons)

if estoque > 0:
    print(f"restou no estoque: {int(estoque)} cupons")
else:
    print("estoque esgotado")
    
if saldo // VALOR_CUPOM != quantidade_cupons:
    print("cupons que faltaram para o ultimo:", int((saldo // VALOR_CUPOM) - quantidade_cupons))
else:
    print("Tudo certo!")