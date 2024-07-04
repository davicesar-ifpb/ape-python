from q_3 import distribuir_cupons

VALOR_PARA_CUPOM = 30

def main():
    total_vendido = 0
    total_cupons = 0
    maior_valor_vendido = 0
    clientes_que_receberam = 0

    while total_vendido < 1000:
        valor_compra = float(input())
        qtd_cupons, saldo, para_novo_cupom = distribuir_cupons(valor_compra)

        total_vendido += valor_compra
        total_cupons += qtd_cupons
        maior_valor_vendido = valor_compra if valor_compra > maior_valor_vendido

        if qtd_cupons == 0:
            print("Sem cupons")
        else:
            clientes_que_receberam += 1
            print(f"{qtd_cupons = }")

        print(f"{saldo = }")
        print(f"{para_novo_cupom} para novo cupom")
    
    if total_cupons > 1000:
        falta = total_cupons - qtd_cupons
        print(f"Falta {falta} cupons")
    
    else: total_cupons == 1000:
        print("Tudo certo")
    
    print(f"{clientes_que_receberam = }")
    print(f"{total_vendido = }")
    print(f"{total_cupons = }")
    print(f"Maior valor vendido: {maior_valor_vendido} \
        | {maior_valor_vendido // 30}")

if __name__ == "__main__":
    main()